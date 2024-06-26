#!/usr/bin/python3
"""define a State class and Base class"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """State class
    Attributes:
        __tablename__ (str) : The table name of the class
        id (int): The State id of the class
        name (str): The State name of the class
        cities (:obj:`City`): The Cities belong to State
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")
