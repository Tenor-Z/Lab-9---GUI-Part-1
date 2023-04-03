#Reused code, reused code everywhere!

from tkinter import *           #Import everything from tkinter because we need it for our input box
from tkinter import ttk      #ttk is used for creating the window and buttons
from tkinter import messagebox      #Messagebox is used for errors
from poke_api import get_pokemon         #And we need the pokeAPI module for querying and getting results.

root = Tk()                #Start up tk
root.title("Pokemon Info Viewer")               #Create the title of our input box
root.resizable(False, False)                    #Make it so that it cannot be resized


#First using Tkinter we must create our window which will be opened
frm_top = ttk.Frame(root)                                           #Initialize making the top of our box
frm_top.grid(row=0, column=0, columnspan=2, pady=10, padx=10)        #The top will be 0,0 and will span to 2 columns (vertically)

frm_btm_left = ttk.LabelFrame(root, text="Info")                    #Create a frame for the Pokemon's info using a labal frame
frm_btm_left.grid(row=1, column=0, sticky=N, padx=(15,0))              #To the grid, stick to the left and go to the first row (not 0)

frm_btm_right = ttk.LabelFrame(root, text="Stats")                      #Create a frame on the right called Stats
frm_btm_right.grid(row=1, column=1, sticky=N, padx=10, pady=(0,10))       #Stick to the right and on the first row (same row as Info)


#-----------------------------------------------------
#Here is where put our input box
#------------------------------------------------------

lbl_name = ttk.Label(frm_top, text="Pokemon Name:")                   #Add a new label called Pokemon Name and put it on the top of the box
lbl_name.grid(row=0, column=0)                               #Put it on 0,0 on the grid

ent_name = ttk.Entry(frm_top)                                        #Create an entry box to input the name of a Pokemon (must be lowercase) using ttk.Entry
ent_name.grid(row=0, column=1, padx=10)                               #Put it next to the lbl_name (row 0, column 1)


#---------------------------------------------------------------------------------------
#Here is where we get input on our input box
#When the Get Info box is clicked, it will get the corresponding Pokemon's information
#---------------------------------------------------------------------------------------

def handle_get_info_btn_click():

    name = ent_name.get()           #Get the input from the entry
    name.strip()                    #Remove all whitespaces
    if name.isupper() == True:           #If it is capitlize, attempt to lowercase it so it can be queried with the API
        name.lower()
    if name == "":                          #If there is nothing in the input
        return                           #Return and do nothing


    poke_info = get_pokemon(name)       #Query the API for the given name in the input box
    if poke_info is None:                                   #If there is nothing there or the Pokemon is invalid
        error = f"Unable to get information from PokeAPI about {name}"          #Display an error message BUT DON'T QUIT
        messagebox.showinfo(title="Error", message=error, icon='error')


    #-----------------------------------------------------
    #The following are information variables used to fill
    #in blanks on the GUI. For example, height_value gets
    #the height from the information we get back from the API
    #and so forth
    #------------------------------------------------------

    lbl_height_value['text'] = f"{poke_info['height']} dm"          #For some reason, the API measures it out in DM and HG
    lbl_weight_value['text'] = f"{poke_info['weight']} hg"      #Both height and weight are available in the main list of the results
    
    #Since Pokemon can have two types, we must query for each type a Pokemon may have
    poke_type = [type['type']['name'] for type in poke_info['types']]               #For every type in the types list (only want the 'name' value in the list so it iterates for each type the pokemon has)
    poke_type_list = ', '.join(poke_type).title()                                   #If there is more than one type, join the two together by a comma, and capitalize both
    lbl_types_value['text'] = poke_type_list                                        #And this value will be used to fill in the GUI

    prg_hp['value'] = poke_info['stats'][0]['base_stat']              #All Pokemon stats can be found in the [base_stat] list with their indexes listed in the code
    prg_attack['value'] = poke_info['stats'][1]['base_stat']            #THEY MUST BE VALUES, as specified
    prg_defense['value'] = poke_info['stats'][2]['base_stat']           #Once they find the results, it will be added to the display bars in the GUI
    prg_spattack['value'] = poke_info['stats'][3]['base_stat']
    prg_spdefense['value'] = poke_info['stats'][4]['base_stat']
    prg_speed['value'] = poke_info['stats'][5]['base_stat']

    return

#Here is where we create the button that gets a Pokemon's info
btn_getinfo = ttk.Button(frm_top, text="Get info", command=handle_get_info_btn_click)       #Command indicates what to do upon clicking
btn_getinfo.grid(row=0, column=2)                                   #Put it next to Pokemon name label


#Create the height label and place it to the bottom left frame
lbl_height = ttk.Label(frm_btm_left, text="Height:")
lbl_height.grid(row=0, column=0)

#Add the height value to the GUI (default is TBD)
lbl_height_value = ttk.Label(frm_btm_left, text="TBD")
lbl_height_value.grid(row=0, column=1)

#Create the weight label and place it on the bottom left frame
lbl_weight = ttk.Label(frm_btm_left, text="Weight:")
lbl_weight.grid(row=1, column=0)

#Add the weight value fetched earlier to the GUI (default is TBD)
lbl_weight_value = ttk.Label(frm_btm_left, text="TBD")
lbl_weight_value.grid(row=1, column=1)

#Create the HP value and add it to the right frame (the value adding is out of order for some reason, added it in the wrong place lol)
lbl_hp = ttk.Label(frm_btm_right, text='HP:')
lbl_hp.grid(row=0, column=0)

#Create the types label and put it to the left frame
lbl_types = ttk.Label(frm_btm_left, text="Type(s):")
lbl_types.grid(row=2, column=0, sticky=E)

#Get the types value from what was estimated earlier and put it in its spot. (default is TBD)
lbl_types_value = ttk.Label(frm_btm_left, text="TBD")
lbl_types_value.grid(row=2, column=1, stick=W)

#Get the value of HP as a progress bar (maximum length is 255 because Pokemon's stats don't go over that amount)
prg_hp = ttk.Progressbar(frm_btm_right, orient=HORIZONTAL, length=200, maximum=255)
prg_hp.grid(row=0, column=1, padx=(0,5))

#Create the attack label and put it on the right frame
lbl_attack = ttk.Label(frm_btm_right, text='Attack:')
lbl_attack.grid(row=1, column=0)

#Generate the progress bar estimated above from the PokeAPI results
prg_attack = ttk.Progressbar(frm_btm_right, orient=HORIZONTAL, length=200, maximum=255)
prg_attack.grid(row=1, column=1, pady=5, padx=(0,5))

#Create the defense label and put it on the right frame
lbl_defense = ttk.Label(frm_btm_right, text='Defense:')
lbl_defense.grid(row=2, column=0)

#Generate the defense progress bar estimated from PokeAPI results
prg_defense = ttk.Progressbar(frm_btm_right, orient=HORIZONTAL, length=200, maximum=255)
prg_defense.grid(row=2, column=1, pady=5, padx=(0,5))

#Create the special attack label and put it on the right frame
lbl_spattack = ttk.Label(frm_btm_right, text='Special Attack:')
lbl_spattack.grid(row=3, column=0)

#Generate progress bar from estimated PokeAPI results
prg_spattack = ttk.Progressbar(frm_btm_right, orient=HORIZONTAL, length=200, maximum=255)
prg_spattack.grid(row=3, column=1, pady=(0,5), padx=(0,5))

#Create the special defense label and put it on the right frame
lbl_spdefense = ttk.Label(frm_btm_right, text='Special Defense:')
lbl_spdefense.grid(row=4, column=0)

#Generate progress bar from estimated PokeAPI results
prg_spdefense = ttk.Progressbar(frm_btm_right, orient=HORIZONTAL, length=200, maximum=255)
prg_spdefense.grid(row=4, column=1, pady=(0,5), padx=(0,5))

#Create the speed label and put it on the right frame
lbl_speed = ttk.Label(frm_btm_right, text='Speed:')
lbl_speed.grid(row=5, column=0)

#Generate the progress bar from estimated Pokemon Results
prg_speed = ttk.Progressbar(frm_btm_right, orient=HORIZONTAL, length=200, maximum=255)
prg_speed.grid(row=5, column=1, pady=(0,5), padx=(0,5))

root.mainloop() #Loop until the window is manually closed