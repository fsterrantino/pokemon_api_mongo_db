from configparser import ConfigParser

def read_db_params():
    parser = ConfigParser()
    parser.read('/opt/config.ini')

    section = 'postgresql'
    db_params = {}

    db_params['host'] = parser.get(section, 'host')
    db_params['user'] = parser.get(section, 'user')
    db_params['password'] = parser.get(section, 'password')
    db_params['port'] = parser.get(section, 'port')
    db_params['database'] = parser.get(section, 'database')

    return db_params