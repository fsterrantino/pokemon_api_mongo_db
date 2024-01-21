import pandas as pd

def read_df(archive_name):

    path = '/opt/Output/'

    df = pd.read_csv(path + archive_name, sep=";")
    return df