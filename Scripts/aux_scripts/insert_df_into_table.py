def insert_df_into_table(engine, df, table_name):

    df.to_sql(table_name, engine, index=False, if_exists='replace', method='multi')
    print(f"Data from DataFrame successfully inserted into table '{table_name}'")