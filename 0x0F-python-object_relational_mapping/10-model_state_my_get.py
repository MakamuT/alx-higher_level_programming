#!/usr/bin/python3
"""
prints the State object with the name passed
as argument from the database
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import State, Base

if __name__ == '__main__':
    """access to the databese"""

    db_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
                                                              argv[1],
                                                              argv[2],
                                                              argv[3])
    engine = create_engine(db_url)
    Session = sessionmaker(bind=engine)

    session = Session()

    state = session.query(State).filter(State.name == argv[4]).first()
    if state is not None:
        print('{0}'.format(state.id))
    else:
        print("Not found")
