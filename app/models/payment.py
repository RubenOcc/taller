from sqlalchemy import Column, Integer, ForeignKey, Numeric, String, Date, DateTime, func
from connection import Base  # Asegúrate de que `Base = declarative_base()` esté definido en connection.py

class Payment(Base):
    __tablename__ = 'payment'

    payment_id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey('order_request.order_id'), nullable=False)
    amount = Column(Numeric(10, 2), nullable=False)
    payment_method = Column(String(20), nullable=False)
    recipient = Column(String(100), nullable=False)
    payment_date = Column(Date, nullable=False)
    created_at = Column(DateTime, server_default=func.now())
