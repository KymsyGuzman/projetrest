from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session

from app.db.database import SessionLocal
from app.db import models

router = APIRouter()

@router.get("/{city}")
async def read_theaters(city: str, db: Session = SessionLocal()):
    theaters = db.query(models.Theater).filter(models.Theater.city == city).all()
    if not theaters:
        raise HTTPException(status_code=404, detail="No theaters found for this city")
    return theaters