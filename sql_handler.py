import pandas as pd
from sqlalchemy import create_engine

def connect_to_sql(db_uri):
    engine = create_engine(db_uri)
    return engine

def get_sql_data(engine, query):
    df = pd.read_sql(query, engine)
    return df
