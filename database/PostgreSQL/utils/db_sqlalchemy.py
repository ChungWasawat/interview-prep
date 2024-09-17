from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv
import os

metadata = MetaData()
Base = declarative_base()

def db_connect():
    load_dotenv()
    username = os.getenv("SUPABASE_USERNAME")
    password = os.getenv("SUPABASE_PASSWORD")
    dbname = os.getenv("SUPABASE_NAME")
    port = os.getenv("SUPABASE_PORT")
    host = os.getenv("SUPABASE_HOST")
    engine = create_engine(f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{dbname}", echo=False)
    connection = engine.connect()

    return engine, connection


def create_tables(engine):
    metadata.drop_all(engine, checkfirst=True)
    metadata.create_all(engine, checkfirst=True)


def create_tables_orm(engine):
    Base.metadata.drop_all(engine, checkfirst=True)
    Base.metadata.create_all(engine, checkfirst=True)


def create_session(engine):
    Session = sessionmaker(bind=engine)
    session = Session()

    return session