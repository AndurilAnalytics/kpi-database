from anduril_kpi.modules import dataframes

def df_handler(df):
    return dataframes.drop_duplicates(df=df)