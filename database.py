from typing import Optional

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import Table, Column, Integer, String, ForeignKey
from sqlalchemy.orm import registry
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class Person(Base):
    __tablename__ = "person"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(32))
    fullname: Mapped[Optional[str]]
    password: Mapped[str] = mapped_column(String(256))


class Attribute(Base):
    __tablename__ = 'attribute'

class Campaign(Base):
    __tablename__ = "campaign"
    id = Mapped[int] = mapped_column(primary_key=True)


class Character(Base):
    __tablename__ = "character"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(32))


def create_all_tables(engine):
    Base.metadata.create_all(engine)


def load_engine():
    engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)
    return engine
