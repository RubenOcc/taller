from sqlalchemy import Column, Integer, ForeignKey, Text, Numeric, String, DateTime, func
from connection import Base  # Importa el Base declarado en connection.py
from sqlalchemy.orm import relationship

class ExtraItem(Base):
    __tablename__ = 'extra_item'

    item_id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey('order_request.order_id'), nullable=False)
    description = Column(Text, nullable=False)
    cost = Column(Numeric(10, 2), nullable=False)
    status = Column(String(20), nullable=False, default='PENDING')
    created_at = Column(DateTime, server_default=func.now())

    # Si deseas acceder a la orden relacionada desde ExtraItem:
    # order = relationship('OrderRequest', back_populates='extra_items')  ← opcional
