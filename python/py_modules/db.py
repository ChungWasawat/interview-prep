from dotenv import load_dotenv
import os
import sqlalchemy

def db_connect():
    load_dotenv()
    username = os.getenv("SUPABASE_USERNAME")
    password = os.getenv("SUPABASE_PASSWORD")
    dbname = os.getenv("SUPABASE_NAME")
    port = os.getenv("SUPABASE_PORT")
    host = os.getenv("SUPABASE_HOST")
    engine = sqlalchemy.create_engine(f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{dbname}", echo=True)
    connection = engine.connect()

    return engine, connection