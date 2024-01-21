from aux_scripts.create_sqlalchemy_engine import create_sqlalchemy_engine
from aux_scripts.read_df import read_df
from aux_scripts.insert_df_into_table import insert_df_into_table

def load():
    engine = create_sqlalchemy_engine()

    pokemons_df = read_df('pokemons_df.csv')
    attacks_df = read_df('attacks_df.csv')

    insert_df_into_table(engine, pokemons_df, 'pokemons')
    insert_df_into_table(engine, attacks_df, 'attacks')

