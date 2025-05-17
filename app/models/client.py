from sqlalchemy import Column, Integer, String, Text, DateTime, func
from sqlalchemy.orm import relationship
from connection import Base  # Importas el Base que declaraste en connection.py

class Client(Base):
    __tablename__ = 'client'

    client_id = Column(Integer, primary_key=True)
    first_name = Column(String(100), nullable=False)
    last_name_father = Column(String(100), nullable=False)
    last_name_mother = Column(String(100), nullable=False)
    phone = Column(String(20))
    address = Column(Text)
    reference = Column(Text)
    district = Column(String(100))
    created_at = Column(DateTime, server_default=func.now())

    orders = relationship('OrderRequest', backref='client', cascade="all, delete-orphan")
