from fastapi import FastAPI
from contextlib import asynccontextmanager
from controllers.product_controller import create_product_controller
from dataBase.init_db import init_db
from schemas.Product import ProductCreate, Product


@asynccontextmanager
async def app_lifespan(app: FastAPI):
    await init_db()
    yield

app = FastAPI(lifespan=app_lifespan)

@app.get("/")
async def read_root():
    return {"message": "Hello World"}


@app.post("/products/create/", response_model=Product)
async def create_product(product: ProductCreate):
    return await create_product_controller(product)
