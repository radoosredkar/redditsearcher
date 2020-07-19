from sqlalchemy import Integer, String, Column, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class SubReddit(Base):
    __tablename__ = "subreddit"

    id = Column(Integer, primary_key=True)
    title = Column(String, index=True)
    description = Column(String)
    date_created = Column(String)

    def __repr__(self):
        return f"SubReddit {self.id} {self.title} {self.date_created}"
