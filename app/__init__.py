from fastapi import FastAPI
from app.api import movies, theaters
from app.db.database import engine, Base

# Créer l'application
app = FastAPI()

# Créer les tables de la base de données
Base.metadata.create_all(bind=engine)

# Ajouter les endpoints
app.include_router(movies.router)
app.include_router(theaters.router)