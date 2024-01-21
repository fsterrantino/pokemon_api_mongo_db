from pymongo import MongoClient
from aux_scripts.read_mongodb_params import read_mongodb_params
from aux_scripts.read_json_file import read_json_file
from aux_scripts.insert_json import insert_json

def check_mongodb_results():

    mongodb_params = read_mongodb_params()

    client = MongoClient(mongodb_params['host'], mongodb_params['port'])
    
    database = client[mongodb_params['database']]
    collection = database[mongodb_params['collection']]

    query = {}
    projection = {'id': 1, 'name': 1, 'types': 1}

    results = collection.find(query, projection).limit(5)

    for result in results:
        print(result)

    client.close()
