from configparser import ConfigParser

def read_request_params():
    parser = ConfigParser()
    parser.read('/opt/config.ini')

    section = 'request_params'
    request_params = {}

    request_params['start_pokemon_id'] = int(parser.get(section, 'start_pokemon_id'))
    request_params['end_pokemon_id'] = int(parser.get(section, 'end_pokemon_id'))

    return request_params