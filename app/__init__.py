from flask import Flask
from connection import engine, Base
import logging
from app.routes.routes import main_bp
from app.routes.clients import client

def create_app():
    app = Flask(__name__)

    logging.basicConfig(level=logging.DEBUG)

    # Crear las tablas si no existen
    with app.app_context():
        try:
            # Solo creamos las tablas si no existen
            Base.metadata.create_all(bind=engine)
            logging.info("✅ Tablas revisadas/creadas correctamente.")
        except Exception as e:
            logging.error(f"❌ Error al crear las tablas: {e}")

    # Import and register Blueprints
    app.register_blueprint(main_bp, url_prefix='/')
    app.register_blueprint(client, url_prefix='/client')

    return app
