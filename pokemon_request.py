#Programme pour Récupérer les données SDk de Swiftz!!
import requests

base_url="https://pokeapi.co/api/v2/"

def pokemon_get_info(name):
    url = f'{base_url}/pokemon/{name}'
    response = requests.get(url)
    
    # Status de la réponse 
    if response.status_code == 200 :
        pokemon_data =response.json()
        return pokemon_data

    else:
        print(f'Failed to retreived data {response.status_code}')

pokemon_name = "greninja"
pokemon_info = pokemon_get_info(pokemon_name)

# Récupération des informations voulu
if pokemon_info:
    print(f'Name: {pokemon_info["name"].capitalize()}')
    print(f'Weight: {pokemon_info["weight"]}')
    print(f'Height: {pokemon_info["height"]}')
    print(f'Id: {pokemon_info["id"]}')