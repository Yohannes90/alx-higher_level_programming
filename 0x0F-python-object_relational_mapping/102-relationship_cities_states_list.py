#!/usr/bin/python3
"""lists all City objects from the database hbtn_0e_101_usa
"""

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

    for state in session.query(State).order_by(State.id):
        for city in state.cities:
            print("{}: {} -> {}".format(city.id, city.name, state.name))
