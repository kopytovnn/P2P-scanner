from sqlalchemy import MetaData, Table, String, Integer, Column, Text, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from database.models.base import Base

class User(Base):
    __tablename__ = 'User'

    id = Column(Integer, nullable=False, unique=True, primary_key=True, autoincrement=True)
    telegram_id = Column(String(), nullable=False)

    name = Column(String(), nullable=True)
    status = Column(String(), nullable=True) #  blacklist, user, premium

    demands = relationship("Demand")

    def __repr__(self):
        return "<{0.__class__.__name__}(id={0.id!r})>".format(self)


class Demand(Base):
    __tablename__ = "Demand"
    id = Column(Integer, primary_key=True)
    message = Column(String(), nullable=False)

    type = Column(String(), nullable=True)
    status = Column(String(), nullable=True)

    owner = Column(Integer, ForeignKey("User.telegram_id"))
