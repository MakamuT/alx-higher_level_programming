#!/usr/bin/pyhton3
"""Lists all State objects from the database"""

from sqlalchemy inmport create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State, Base
from sys import argv

if __name__ == "__main__":
    """access database"""

    db_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(argv[1],
                                                              argv[2],
                                                              argv[3])
    engine = create_engine(db_url)
    Session = sessionmaer(bind=engine)

    session = Session()

    for instance in session.query(State).order_by(State.id):
        print('{0}: {1}'.format(instance.id, instance.name))
