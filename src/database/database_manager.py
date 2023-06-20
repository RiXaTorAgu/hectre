from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class DatabaseManager:

    def __init__(self, Base, connection_url='sqlite:///data/database.db'):

        self.Base = Base
        self.connection_url = connection_url
        self.engine = create_engine(self.connection_url)
    
    def create_database(self):

        self.Base.metadata.create_all(bind=self.engine)

    def execute_commands(self, commands):

        Session = sessionmaker(bind=self.engine)
        session = Session()

        try:

            commands(session)
            session.commit()

        except Exception as exception:

            session.rollback()
            print("An error occurred:", str(exception))

        finally:

            session.close()
