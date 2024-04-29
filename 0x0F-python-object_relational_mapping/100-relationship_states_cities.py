#!/usr/bin/python3
"""prints all the City objects"""
from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == '__main__':
    """access to the database"""

    db_url = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                                                              argv[1],
                                                              argv[2],
                                                              argv[3])
    engine = create_engine(db_url)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    session = Session()
    cal_state = State(name='Calfornia')
    sfr_city = City(name='San Francisco')
    cal_state.cities.append(sfr_city)

    session.add(cal_state)
    session.commit()
    session.close()
