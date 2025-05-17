from sqlalchemy.orm import Session
from sqlalchemy import text
from connection import engine

class ClientRepository:
    @staticmethod
    def get_all_clients():
        with Session(engine) as session:
            query = text("""
                SELECT client_id, first_name, last_name_father, last_name_mother,
                       phone, address, reference, district, created_at
                FROM client
                ORDER BY created_at DESC
            """)
            result = session.execute(query).fetchall()
            return result

    @staticmethod
    def register_client(data):
        with Session(engine) as session:
            query = text("""
                INSERT INTO client (first_name, last_name_father, last_name_mother,
                                    phone, address, reference, district)
                VALUES (:first_name, :last_name_father, :last_name_mother,
                        :phone, :address, :reference, :district)
                RETURNING client_id
            """)
            result = session.execute(query, data)
            session.commit()
            return result.scalar()
