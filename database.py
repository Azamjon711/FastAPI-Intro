from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
import os
from dotenv import load_dotenv
load_dotenv()


ENGINE = create_engine(f"{os.getenv("DB")}://{os.getenv("DB_USER"):{os.getenv("DB_PASSWORD")}@localhost/{os.getenv("DB_NAME")}", echo=True)

Base = declarative_base()
session = sessionmaker()





