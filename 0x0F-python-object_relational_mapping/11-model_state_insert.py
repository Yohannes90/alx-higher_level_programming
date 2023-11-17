#!/usr/bin/python3

""" adds the State object “Louisiana” to the database hbtn_0e_6_usa
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

    session.add(State(name="Louisiana"))
    new_state = session.query(State).filter_by(name="Louisiana").first()
    print(new_state.id)
    session.commit()

    session.close()
