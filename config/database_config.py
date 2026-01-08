import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv



# Load environment variables from .env file
load_dotenv()

username = os.environ['DATABASE_USERNAME']
password = os.environ['DATABASE_PASSWORD']
host = os.environ['DATABASE_HOST']
port = os.environ['DATABASE_PORT']
database = os.environ['DATABASE_NAME']
database_type = os.environ['DATABASE_TYPE']

db_url = f"{database_type}://{username}:{password}@{host}:{port}/{database}"

engine = create_engine(db_url)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base = declarative_base()