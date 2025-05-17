from sqlalchemy import Column, Integer, ForeignKey, String, Text, Numeric, Date, DateTime, func
from connection import Base  # Este debe ser el declarative_base() definido en connection.py

class OrderDetail(Base):
    __tablename__ = 'order_detail'

    detail_id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey('order_request.order_id'), nullable=False)
    brand = Column(String(50))
    description = Column(Text)
    service = Column(String(100), nullable=False)
    unit_price = Column(Numeric(10, 2))
    estimated_delivery = Column(Date)
    status = Column(String(20), nullable=False, default='PENDING')
    created_at = Column(DateTime, server_default=func.now())
