import psycopg2
from aux_scripts.read_db_params import read_db_params

def create_postgres_tables():

    db_params = read_db_params()

    connection = psycopg2.connect(
        dbname = db_params['database'],
        user = db_params['user'], 
        password = db_params['password'], 
        host = db_params['host'], 
        port = db_params['port']
        )
    cursor = connection.cursor()

    # Define SQL statements to create tables
    create_table1_query = """
        CREATE TABLE IF NOT EXISTS pokemons (
            pokemon_id INT PRIMARY KEY,
            pokemon_name VARCHAR(255),
            type1 VARCHAR(50),
            type2 VARCHAR(50),
            weight INT,
            hp INT,
            attack INT,
            defense INT,
            special_attack INT,
            special_defense INT,
            speed INT
        );
    """

    create_table2_query = """
        CREATE TABLE IF NOT EXISTS attacks (
            pokemon_id INT,
            move_name VARCHAR(255),
            level_learned_at INT,
            move_learn_method VARCHAR(50),
            version_group VARCHAR(50)
        );
    """

    # Execute the SQL statements to create tables
    cursor.execute(create_table1_query)
    cursor.execute(create_table2_query)

    # Commit the changes and close the connection
    connection.commit()
    cursor.close()
    connection.close()

    print("Tables created successfully.")