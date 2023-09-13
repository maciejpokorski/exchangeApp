from sqlmodel import SQLModel, create_engine, Session

import os

def setup_db():
    USERNAME = os.getenv("MYSQL_USER")
    PASSWORD = os.getenv("MYSQL_PASSWORD")
    DATABASE = os.getenv("MYSQL_DATABASE")
    DATABASE_URL = f"mysql+mysqlconnector://{USERNAME}:{PASSWORD}@127.0.0.1:3306/{DATABASE}"
    engine = create_engine(DATABASE_URL, echo=True)
    SQLModel.metadata.create_all(bind=engine)
    return Session(engine)