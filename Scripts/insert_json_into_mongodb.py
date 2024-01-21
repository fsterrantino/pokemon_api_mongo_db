from pymongo import MongoClient
from aux_scripts.read_mongodb_params import read_mongodb_params
from aux_scripts.read_json_file import read_json_file
from aux_scripts.insert_json import insert_json

def insert_json_into_mongodb():

    mongodb_params = read_mongodb_params()

    client = MongoClient(mongodb_params['host'], mongodb_params['port'])
    
    # Access the database (creates it if it doesn't exist)
    database = client[mongodb_params['database']]
    
    # Access the collection (creates it if it doesn't exist)
    collection = database[mongodb_params['collection']]

    json_data = read_json_file('/opt/Output/pokemon_data.json')
    insert_json(json_data, collection)