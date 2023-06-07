from flask import session
#from app import app
from dotenv import load_dotenv
from fastapi import FastAPI, Depends
#from app.api.movies import router as movies_router
#from db.models import Movie
from app.db.database import engine, Base, get_db, init_db
load_dotenv()
app = FastAPI()
def init_db():
    Base.metadata.create_all(bind=engine)
@app.on_event("startup")
async def startup_event():
    init_db()

#Création de la base de données 
@app.on_event("startup")
async def startup_event():
    init_db()
@app.get("/")
async def root():
    return {"message": "Hello World"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/movies/{movie_id}")
async def read_movie(movie_id: int):
    db = next(get_db())
    movie = db.query(Movie).filter(Movie.id == movie_id).first()
    if movie is None:
        # Gérer le cas où le film n'est pas trouvé
        pass
    return movie
@app.post("/movies")
async def create_movie(movie: Movie, db: session = Depends(get_db)):
    db.add(movie)
    db.commit()
    db.refresh(movie)
    return movie