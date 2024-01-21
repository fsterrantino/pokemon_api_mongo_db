from aux_scripts.query_all_documents import query_all_documents
from aux_scripts.create_pokemons_and_attacks_dicts import create_pokemons_and_attacks_dicts
from aux_scripts.replace_nan import replace_nan
from aux_scripts.read_mongodb_params import read_mongodb_params
import pandas as pd
from pymongo import MongoClient

# https://pokeapi.co/api/v2/pokemon/2/

def transform():

    mongodb_params = read_mongodb_params()

    client = MongoClient(mongodb_params['host'], mongodb_params['port'])
    database = client[mongodb_params['database']]
    collection = database[mongodb_params['collection']]

    all_documents_list = query_all_documents(collection)

    empty_pokemons_list = []
    empty_attacks_list = []
    pokemons_list, attacks_list = create_pokemons_and_attacks_dicts(all_documents_list, empty_pokemons_list, empty_attacks_list)

    pokemons_df = pd.DataFrame(pokemons_list)
    attacks_df = pd.DataFrame(attacks_list)
    
    pokemons_df = replace_nan(pokemons_df)
    pokemons_df.columns = pokemons_df.columns.str.replace('-', '_')
    attacks_df.columns = attacks_df.columns.str.replace('-', '_')

    pokemons_df.to_csv('/opt/Output/pokemons_df.csv', index=False, encoding="utf-8", sep=";")
    attacks_df.to_csv('/opt/Output/attacks_df.csv', index=False, encoding="utf-8", sep=";")
    print('Dfs generated Ok.')