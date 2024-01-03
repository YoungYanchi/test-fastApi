from fastapi import HTTPException
from schemas.Product import ProductCreate, Product
from services.product_service import create_product_service
import logging

async def create_product_controller(product: ProductCreate):
    try:
        # Вызываем сервис для создания продукта
        new_product = await create_product_service(product)
        # Возвращаем Pydantic модель, созданную из SQLAlchemy модели
        return Product.model_validate(new_product)
    except Exception as e:
        logging.error(f"Error while creating product: {e}")
        raise HTTPException(status_code=400, detail=str(e))
