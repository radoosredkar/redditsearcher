from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine

engine = create_engine(
    "sqlite:////home/rado/software/python3/reddit/migrations/app.db", echo=False
)


Sesson = scoped_session(sessionmaker(bind=engine))
