from dataBase.database import AsyncSessionLocal
from models.Product import ProductModel
from schemas.Product import ProductCreate

async def create_product_service(product_data: ProductCreate):
    async with AsyncSessionLocal() as session:
        new_product = ProductModel(**product_data.model_dump())
        session.add(new_product)
        await session.commit()
        await session.refresh(new_product)
        return new_product
