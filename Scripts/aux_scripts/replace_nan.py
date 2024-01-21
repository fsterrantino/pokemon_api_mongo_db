def replace_nan(df):
    df = df.fillna('-')
    return df