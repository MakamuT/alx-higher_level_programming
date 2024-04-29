#!/usr/bin/python3
"""defines a city class"""

from relationship_state import State, Base
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """City class
    Attributes:
        __tablename__ (str); THe table name of the class
        id (int): The id of the class
        name (str): The name of the class
        state_id (int); The state the city belongs to
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
