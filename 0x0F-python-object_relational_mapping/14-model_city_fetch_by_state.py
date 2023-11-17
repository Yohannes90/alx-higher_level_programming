#!/usr/bin/python3

""" prints all City objects from the database hbtn_0e_14_usa
"""

from sys import argv
from model_state import Base, State
from model_city import City
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

    for state in (session.query(State.name, City.id, City.name)
                  .filter(City.state_id == State.id)):
        print("{}: ({}) {}".format(state[0], state[1], state[2]))

    session.close()
