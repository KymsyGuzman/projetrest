from fastapi import APIRouter
from typing import List
from app.db.models import Movie
from app.db.database import SessionLocal

router = APIRouter()

@router.post("/")
def create_movie(movie: Movie):
    db = SessionLocal()
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