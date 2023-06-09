from fastapi import APIRouter, Depends
from typing import List
from app.db.models import Movie
#from app.db.database import SessionLocal
from app.db.session import SessionLocal
from app.db.database import get_db
from app.core.auth import get_current_active_user

router = APIRouter()

#@router.post("/")
#def create_movie(movie: Movie, current_user=Depends(get_current_active_user)):
#   db = SessionLocal()
#    db.add(movie)
#   db.commit()
#    db.refresh(movie)
#    return movie
@router.post("/")
def create_movie(movie: Movie, db: SessionLocal = Depends(get_db)):
#def create_movie(movie: Movie, current_user=Depends(get_current_active_user)):
    db.add(movie)
    db.commit()
    db.refresh(movie)
    return movie
@router.get("/{movie_id}")
def read_movie(movie_id: int):
    db = SessionLocal()
    movie = db.query(Movie).filter(Movie.id == movie_id).first()
    return movie

@router.get("/")
def read_movies(skip: int = 0, limit: int = 100):
    db = SessionLocal()
    movies = db.query(Movie).offset(skip).limit(limit).all()
    return movies