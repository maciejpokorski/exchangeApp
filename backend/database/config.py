from sqlalchemy import create_engine
from sqlmodel import SQLModel, Session
from constants import USERNAME, PASSWORD, DATABASE

MYSQL_URL = f"mysql+mysqlconnector://{USERNAME}:{PASSWORD}@localhost:3306/{DATABASE}"
def get_session(database_url: str = MYSQL_URL):
    engine = create_engine(database_url)
    SQLModel.metadata.create_all(engine)

    with Session(engine) as session:
        yield session