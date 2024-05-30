from fastapi import FastAPI
from auth import auth_router
from category import category_router
from orders import order_router
from product import product_router

app = FastAPI()
app.include_router(auth_router)
app.include_router(category_router)
app.include_router(order_router)
app.include_router(product_router)


@app.get("/")
async def landing():
    return {
        "message": "Hello World"
    }


@app.get("/about")
async def about():
    return {
        "message": "This is about page"
    }


@app.get("/team")
async def team():
    return {
        "message": "This is team page"
    }
