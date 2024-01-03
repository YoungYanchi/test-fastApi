# init_db.py
from dataBase.database import Base
from .database import engine
from models.Product import ProductModel
from models.Category import Category

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
