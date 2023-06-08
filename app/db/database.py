
from sqlalchemy.orm import Session

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
import app
from app.core.config import settings

#from app.db.session import SessionLocal
from sqlalchemy.orm import sessionmaker


#DATABASE_URL = "sqlite:///./test.db"  # Ce serait votre URL de base de données
#DATABASE_URL=postgresql://username:password@host:port/database_name
DATABASE_URL="postgresql://postgres:postgres@localhost:5432/cinema"
engine = create_engine(
    DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
#engine = create_engine(settings.SQLALCHEMY_DATABASE_URI)
Base = declarative_base()
Base.metadata.bind = engine

def get_db() -> Session:
    from app.db.session import SessionLocal  # Importation différée
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


