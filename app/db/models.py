from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel

class MovieBase(BaseModel):
    title: str
    duration: int
    language: str
    director: str
    age_minimum: int

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

class ScheduleCreate(ScheduleBase):
    movie_id: int
    theater_id: int

class Schedule(ScheduleBase):
    id: int
    movie: Movie
    theater: Theater

    class Config:
        orm_mode = True