from sqlalchemy import Integer, String, Column, Date
from sqlalchemy.ext.declarative import declarative_base
from db import Sesson


Base = declarative_base()
Base.query = Sesson.query_property()


class SubRedditModel(Base):
    __tablename__ = "subreddit"

    id = Column(Integer, primary_key=True)
    title = Column(String, index=True)
    description = Column(String)
    date_created = Column(String)
    flair = Column(String)

    def __repr__(self):
        return f"SubReddit {self.id} {self.title} {self.flair} {self.date_created}"
