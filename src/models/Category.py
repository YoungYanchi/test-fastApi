from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from dataBase.database import Base

# Создаем асинхронный базовый класс для наших моделей

class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)

    products = relationship("ProductModel", back_populates="category")

