#!/usr/bin/python3
"""prints the first State object from the database"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State, Base
from sys import argv

if __name__ == "__main__":
    """access to the database"""

    db_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
                                                              argv[1],
                                                              argv[2],
                                                              argv[3])

    engine = create_engine(db_url)
    Session = sessionmaker(bind=engine)

    session = Session()

    state = session.query(State).order_by(State.id).first()
    if state is not None:
        print('{0}: {1}'.format(state.id, state.name))
    else:
        print("Nothing")
