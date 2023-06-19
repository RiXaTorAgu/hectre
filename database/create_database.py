from sqlalchemy import create_engine

from model import Base

if __name__ == '__main__':

    engine = create_engine('sqlite:///database.db')
    Base.metadata.create_all(bind=engine)