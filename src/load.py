from sqlalchemy import create_engine
from src.config import DATABASE_URL

def load_data(df, table_name="movie_ratings"):
    engine = create_engine(DATABASE_URL)
    df.to_sql(table_name, engine, if_exists="replace", index=False)
    print(f"Loaded {len(df)} rows into '{table_name}'")
