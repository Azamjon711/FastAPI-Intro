from fastapi import FastAPI
from auth import auth_router

app = FastAPI()
app.include_router(auth_router)


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
