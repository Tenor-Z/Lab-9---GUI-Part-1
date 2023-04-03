import requests

poke_api_URL = 'https://pokeapi.co/'        #The URL for the PokeApi module (free to use)


def main():  
    pokemon = get_pokemon("vaporeon")          #Get the Pokemon named in the first argument (default is Vaporeon)
    print(pokemon) 
    
        
def get_pokemon(search_term):

    poke_Search_URL = f'https://pokeapi.co/api/v2/pokemon/{search_term}'             #This is the URL used to look for a Pokemon based on its name


    header_params = {                                                   #Throw in these parameters when searching to limit the entity down to a Pokemon
        'Accept': 'application/json',
        'entity': 'pokemon',
    }

    print(f'Grabbing info about {search_term}...',  end=' ')
    resp_msg = requests.get(poke_Search_URL, headers=header_params)     #Make our search combining the URL and the header parameters above
    

    if resp_msg.ok:
        print('Success!!')
        body_dict = resp_msg.json()                                                     #Convert the data into a list
        #poke_list = [ability['ability']['name']for ability in body_dict['abilities']]      #For every ability in the data (everything with the name Abilities), using the name key for each, add it to a dictionary
        return body_dict    

    else:
        print('Failure')
        print(f'{resp_msg.status_code} ({resp_msg.reason})')
        print(f'Error: {resp_msg.text}')
    return None



if __name__ == '__main__':
    main()