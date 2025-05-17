from sqlalchemy import Column, Integer, ForeignKey, String, Date, DateTime, func
from sqlalchemy.orm import relationship
from connection import Base  # Asegúrate que `Base = declarative_base()` esté definido en connection.py

class OrderRequest(Base):
    __tablename__ = 'order_request'

    order_id = Column(Integer, primary_key=True)
    client_id = Column(Integer, ForeignKey('client.client_id'), nullable=False)
    received_date = Column(Date, nullable=False)
    status = Column(String(20), nullable=False, default='IN_PROGRESS')
    created_at = Column(DateTime, server_default=func.now())

    # Relaciones
    details = relationship('OrderDetail', backref='order', cascade="all, delete-orphan")
    payments = relationship('Payment', backref='order', cascade="all, delete-orphan")
    extra_items = relationship('ExtraItem', backref='order', cascade="all, delete-orphan")
