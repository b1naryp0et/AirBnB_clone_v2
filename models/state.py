#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(BaseModel, Base):
    """This is the class for State
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    """TODO:
    for DBStorage: class attribute cities must represent a relationship with
    the class City. If the State object is deleted, all linked City objects
    must be automatically deleted. Also, the reference from a City object to
    his State should be named state
    for FileStorage: getter attribute cities that returns the list of City
    instances with state_id equals to the current State.id => It will be the
    FileStorage relationship between State and City
    """
