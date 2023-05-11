from fastapi import APIRouter
from typing import List
from app.db.models import Theater, Movie
from app.db.database import SessionLocal

router = APIRouter()

@router.get("/{theater_id}")
def read_theater(theater_id: int):
    db = SessionLocal()
    theater = db.query(Theater).filter(Theater.id == theater_id).first()
    return theater

@router.get("/")
def read_theaters(city