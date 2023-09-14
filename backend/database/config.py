from sqlalchemy import create_engine
from sqlmodel import SQLModel, Session
from constants import USERNAME, PASSWORD, DATABASE

MYSQL_URL = f"mysql+mysqlconnector://{USERNAME}:{PASSWORD}@localhost:3306/{DATABASE}"
try:
    engine = create_engine(MYSQL_URL, echo=True)
except Exception as e:
    print(f"Error connecting to MYSQL database: {e}")
finally:
    engine = create_engine(
        f"sqlite:///{DATABASE}.db", connect_args={"check_same_thread": False}
    )

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session