#!/usr/bin/python3

""" prints the State object with the name passed as argument from hbtn_0e_6_usa
"""

from sys import argv
from model_state import Base, State
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

    state = session.query(State).where(State.name == (argv[4], ))
    try:
        print(state[0].id)
    except IndexError:
        print("Not found")

    session.close()
