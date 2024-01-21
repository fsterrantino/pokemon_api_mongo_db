import json

def save_to_json(data, filename):
    path = '/opt/Output/'

    with open(path + filename, 'w') as json_file:
        json.dump(data, json_file, indent=2)

    print(f'Data saved to {path + filename}')