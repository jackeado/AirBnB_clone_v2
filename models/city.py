#!/usr/bin/python3
"""This is the city class"""
from models.base_model import BaseModel, Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
import os

class City(BaseModel):
    """This is the class for City
    Attributes:
        state_id: The state id
        name: input name
    """
    __tablename__ = "cities"

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        places = relationship("Place", backref="cities",
                              cascade="all, delete-orphan")
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        name = Column(String(128), nullable=False)
    elif os.getenv('HBNB_TYPE_STORAGE') == 'file':
        state_id = ''
        name = ''
