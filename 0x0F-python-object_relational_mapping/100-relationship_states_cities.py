#!/usr/bin/python3

""" create State “California” with City “San Francisco” from hbtn_0e_100_usa"""

from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

if __name__ == "__main__":

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            argv[1], argv[2], argv[3]
        )
    )
    Base.metadata.create_all(engine)
    session = Session(engine)

    newState = State(name="California")
    newCity = City(name="San Francisco")
    newState.cities.append(newCity)

    session.add(newState)
    session.add(newCity)

    session.commit()
    session.close()
