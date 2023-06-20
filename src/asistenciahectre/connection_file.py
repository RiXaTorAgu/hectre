from sqlalchemy import create_engine

db_url = "sqlite:///database/database.db"
engine = create_engine(db_url)