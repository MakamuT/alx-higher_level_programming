#!/usr/bin/python3
"""changes the name of a State object from the database"""

from model_state import State, Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sys import argv

if __name__ == '__main__':
    """updates the database"""

    db_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
                                                              argv[1],
                                                              argv[2],
                                                              argv[3])
    engine = create_engine(db_url)
    Session = sessionmaker(bind=engine)

    session = Session()

    state = session.query(State).filter(State.id == 2).first()
    state.name = "New Mexico"
    session.commit()

    session.close()
