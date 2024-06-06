from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
import os
from dotenv import load_dotenv
load_dotenv()


ENGINE = create_engine("postgresql://postgres:13050@localhost/fastapi", echo=True)

Base = declarative_base()
session = sessionmaker()





