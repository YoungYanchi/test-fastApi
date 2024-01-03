from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from dataBase.database import Base

# Создаем асинхронный базовый класс для наших моделей

class ProductModel(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    price = Column(Float)
    color = Column(String)
    available = Column(Boolean, default=True)
    category_id = Column(Integer, ForeignKey('categories.id'))

    category = relationship("Category", back_populates="products")
