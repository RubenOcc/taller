
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import logging
from sqlalchemy.ext.declarative import declarative_base

# Configuración del logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Cadena de conexión directamente
DATABASE_URI = 'postgresql+psycopg2://postgres:admin@localhost:5432/tailor_db'
engine = create_engine(DATABASE_URI)

try:
    with engine.connect() as conn:
        logger.debug("✅ Conexión a la base de datos exitosa.")
except Exception as e:
    logger.fatal(f"❌ Error fatal al conectar a la base de datos: {e}")
    raise

# Session maker
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()
