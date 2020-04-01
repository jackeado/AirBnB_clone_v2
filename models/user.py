#!/usr/bin/python3
"""This is the user class"""
from models.base_model import BaseModel


class User(BaseModel):
    """This is the class for user
    Attributes:
        email: email address
        password: password for you login
        first_name: first name
        last_name: last name
    """
    __tablename__ = 'users'
    
    email = Column(String(128),unique=True)
    password = Column(String(128))
    first_name = Column(String(128))
    last_name = Column(String(128))
