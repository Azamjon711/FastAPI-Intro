from database import ENGINE, Base
from models import Users, Category, Product, Orders

Base.metadata.create_all(ENGINE)

