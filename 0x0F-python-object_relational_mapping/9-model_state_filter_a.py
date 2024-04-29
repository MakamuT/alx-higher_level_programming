#!/usr/bin/python3
"""lists all State objects that contain the letter a from the database"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State, Base

if __name__ == '__main__':
    """access to the database"""

    db_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
                                                              argv[1],
                                                              argv[2],
                                                              argv[3])

    engine = create_engine(db_url)
    Session = sessionmaker(bind=engine)

    session = Session()

    states = session.query(State).filter(State.name.contains('a'))
    if states is not None:
        for state in states:
            print('{0}: {1}'.format(state.id, state.name))
