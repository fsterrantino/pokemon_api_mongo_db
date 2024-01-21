import psycopg2
from psycopg2 import sql
from aux_scripts.read_db_params import read_db_params
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

def create_postgres_database():

    db_params = read_db_params()

    connection = psycopg2.connect(
        user = db_params['user'], 
        password = db_params['password'], 
        host = db_params['host'], 
        port = db_params['port']
        )
    
    connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = connection.cursor()

    cursor.execute(sql.SQL("SELECT 1 FROM pg_database WHERE datname = %s"), (db_params['database'],))
    exists = cursor.fetchone()

    if not exists:
        create_database_query = sql.SQL(f"CREATE DATABASE {db_params['database']}").as_string(cursor)
        cursor.execute(create_database_query)
        print("DB created successfully.")
    else:
        print('DB already exists.')

    cursor.close()
    connection.close()