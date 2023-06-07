
from sqlalchemy.orm import Session

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
import app
from app.core.config import settings

#from app.db.session import SessionLocal

engine = create_engine(settings.SQLALCHEMY_DATABASE_URI)
Base = declarative_base()
Base.metadata.bind = engine

def get_db() -> Session:
    from app.db.session import SessionLocal  # Importation différée
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


