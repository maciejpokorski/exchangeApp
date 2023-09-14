from sqlalchemy import create_engine
from sqlmodel import SQLModel, Session
from constants import USERNAME, PASSWORD, DATABASE

MYSQL_URL = f"mysql+mysqlconnector://{USERNAME}:{PASSWORD}@db:3306/{DATABASE}"
engine = create_engine(MYSQL_URL, echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session(database_url: str = MYSQL_URL):
    with Session(engine) as session:
        yield session