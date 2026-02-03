#!/usr/bin/python3
"""Print all City objects from the database"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            username, password, database
        ),
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    results = session.query(State, City).filter(
        City.state_id == State.id
    ).order_by(City.id).all()

    for state, city in results:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()
