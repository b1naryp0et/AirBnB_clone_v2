#!/usr/bin/python3
"""This is the city class"""
from models.base_model import BaseModel
from models.state import State
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(BaseModel, Base):
    """This is the class for City
    """
    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey(State.id), nullable=False)
    # foreign key might need more work
