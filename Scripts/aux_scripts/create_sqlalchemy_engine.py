from sqlalchemy import create_engine
from aux_scripts.read_db_params import read_db_params
from sqlalchemy.exc import OperationalError

def create_sqlalchemy_engine():
    db_params = read_db_params()
    try:
        engine = create_engine(
            f"postgresql+psycopg2://{db_params['user']}:{db_params['password']}@{db_params['host']}:{db_params['port']}/{db_params['database']}"
        )

        return engine
    
    except OperationalError as e:
        raise Exception(f"Error creating the database engine: {e}")

