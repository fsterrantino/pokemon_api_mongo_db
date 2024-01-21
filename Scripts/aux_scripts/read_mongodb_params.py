from configparser import ConfigParser

def read_mongodb_params():
    parser = ConfigParser()
    parser.read('/opt/config.ini')

    section = 'mongo'
    mongodb_params = {}

    mongodb_params['host'] = parser.get(section, 'host')
    mongodb_params['database'] = parser.get(section, 'database')
    mongodb_params['port'] = int(parser.get(section, 'port'))
    mongodb_params['collection'] = parser.get(section, 'collection')

    return mongodb_params
