from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String,Boolean
from app.db.database import Base
class MovieBase(BaseModel):
    title: str
    duration: int
    language: str
    director: str
    age_minimum: int



class Movie(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    # Ajoutez d'autres colonnes pour stocker les informations des films
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
class MovieCreate(MovieBase):
    pass

class Movie(MovieBase):
    id: int
    theaters: List["Theater"] = []

    class Config:
        orm_mode = True

class TheaterBase(BaseModel):
    name: str
    address: str

class TheaterCreate(TheaterBase):
    pass

class Theater(TheaterBase):
    id: int
    schedules: List["Schedule"] = []

    class Config:
        orm_mode = True


class ScheduleBase(BaseModel):
    start_time: datetime
    end_time: datetime
    day_of_week: int  # 0 pour Lundi, 1 pour Mardi, etc.

class ScheduleCreate(ScheduleBase):
    movie_id: int
    theater_id: int

class Schedule(ScheduleBase):
    id: int
    movie: Movie
    theater: Theater

    class Config:
        orm_mode = True