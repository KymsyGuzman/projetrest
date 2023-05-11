from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from .database import Base

class Movie(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    duration = Column(Integer)
    language = Column(String)
    director = Column(String)
    age_minimum = Column(Integer)
    theaters = relationship("Theater", secondary="schedules")

class Theater(Base):
    __tablename__ = "theaters"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    address = Column(String)
    schedules = relationship("Schedule", back_populates="theater")

class Schedule(Base):
    __tablename__ = "schedules"

    movie_id = Column(Integer, ForeignKey("movies.id"), primary_key=True)
    theater_id = Column(Integer, ForeignKey("theaters.id"), primary_key=True)
    start_time = Column(DateTime)
    end_time = Column(DateTime)
    theater = relationship("Theater", back_populates="schedules")