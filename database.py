from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
import os
from dotenv import load_dotenv
load_dotenv()


ENGINE = create_engine("postgresql://'db_user':'db_password'@localhost/'db_name'", echo=True)

Base = declarative_base()
session = sessionmaker()





