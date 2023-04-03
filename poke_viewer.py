from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from poke_api import get_pokemon

root = Tk()
root.title("Pokemon Info Viewer")
root.resizable(False, False)


frm_top = ttk.Frame(root)
frm_top.grid(row=0, column=0, columnspan=2, pady=10, padx=10)

frm_btm_left = ttk.LabelFrame(root, text="Info")
frm_btm_left.grid(row=1, column=0, sticky=N, padx=(10,0))

frm_btm_right = ttk.LabelFrame(root, text="Stats")
frm_btm_right.grid(row=1, column=1, sticky=N, padx=10, pady=(0,10))

lbl_name = ttk.Label(frm_top, text="Pokemon Name:")
lbl_name.grid(row=0, column=0)

ent_name = ttk.Entry(frm_top)
ent_name.grid(row=0, column=1, padx=10)

def handle_get_info_btn_click():

    name = ent_name.get()
    if name == "":
        return


    poke_info = get_pokemon(name)
    if poke_info is None:
        error = f"Unable to get information from PokeAPI about {name}"
        messagebox.showinfo(title="Error", message=error, icon='error')

    lbl_height_value['text'] = f"{poke_info['height']} dm"

    prg_hp['value'] = poke_info['stats'][0]['base_stat']
    prg_attack['value'] = poke_info['stats'][1]['base_stat']
    prg_defense['value'] = poke_info['stats'][2]['base_stat']

    return

btn_getinfo = ttk.Button(frm_top, text="Get info", command=handle_get_info_btn_click)
btn_getinfo.grid(row=0, column=2)

lbl_height = ttk.Label(frm_btm_left, text="Height:")
lbl_height.grid(row=0, column=0)

lbl_height_value = ttk.Label(frm_btm_left, text="TBD")
lbl_height_value.grid(row=0, column=1)

lbl_hp = ttk.Label(frm_btm_right, text='HP:')
lbl_hp.grid(row=0, column=0, sticky=E)

prg_hp = ttk.Progressbar(frm_btm_right, orient=HORIZONTAL, length=200, maximum=255)
prg_hp.grid(row=0, column=1, padx=(0,5))

lbl_attack = ttk.Label(frm_btm_right, text='Attack:')
lbl_attack.grid(row=1, column=0, sticky=E)

prg_attack = ttk.Progressbar(frm_btm_right, orient=HORIZONTAL, length=200, maximum=255)
prg_attack.grid(row=1, column=1, pady=5, padx=(0,5))

lbl_defense = ttk.Label(frm_btm_right, text='Defense:')
lbl_defense.grid(row=2, column=0)

prg_defense = ttk.Progressbar(frm_btm_right, orient=HORIZONTAL, length=200, maximum=255)
prg_defense.grid(row=2, column=1, pady=(0,5), padx=(0,5))
root.mainloop()