import psycopg2
from psycopg2 import sql
from aux_scripts.read_db_params import read_db_params

def check_postgre_results():

    db_params = read_db_params()

    connection = psycopg2.connect(
        dbname = db_params['database'],
        user = db_params['user'], 
        password = db_params['password'], 
        host = db_params['host'], 
        port = db_params['port']
        )
    
    cursor = connection.cursor()

    query_code = '''
    SELECT * FROM pokemons LIMIT 10;'''

    query = sql.SQL(query_code)
    cursor.execute(query)

    results = cursor.fetchall()
    for row in results:
        print(row)

    cursor.close()
    connection.close()