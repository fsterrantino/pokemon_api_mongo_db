import requests

def pokemon_api_request(start_pokemon_id, end_pokemon_id, pokemon_data_list):

    for pokemon_id in range(start_pokemon_id, end_pokemon_id + 1):
        url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_id}/'
        response = requests.get(url)

        if response.status_code == 200:
            pokemon_data = response.json()
            pokemon_data_list.append(pokemon_data)
            print(f"Retrieved data for Pokemon {pokemon_id}")
        else:
            print(f"Failed to retrieve data for Pokemon {pokemon_id}. Status code: {response.status_code}")
