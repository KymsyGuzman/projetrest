from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = "sqlite:///./test.db"  # or any other database URL

engine = create_engine(
    DATABASE_URL
)

# sessionmaker creates a factory that generates new Session objects when called
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
