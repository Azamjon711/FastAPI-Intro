# from fastapi import FastAPI
# from pydantic import BaseModel
#
#
# app = FastAPI()
#
#
# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#
#
# @app.get('/')
# async def index():
#     return {
#         "message": "index api"
#     }
#
#
# @app.post('/items/')
# async def create_item(item: Item) -> Item:
#     return item
#
#
# @app.get('/items/')
# async def read_items(item: Item) -> Item:
#     return item
#
