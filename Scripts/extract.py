from aux_scripts.save_to_json import save_to_json
from aux_scripts.read_request_params import read_request_params
from aux_scripts.pokemon_api_request import pokemon_api_request

def extract():
    request_params = read_request_params()
    start_pokemon_id = request_params['start_pokemon_id']
    end_pokemon_id = request_params['end_pokemon_id']

    pokemon_data_list = []
    pokemon_api_request(start_pokemon_id, end_pokemon_id, pokemon_data_list)

    save_to_json(pokemon_data_list, 'pokemon_data.json')