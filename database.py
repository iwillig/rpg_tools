from typing import Optional
from typing import List
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import Table, Column, Integer, String, ForeignKey
from sqlalchemy.orm import registry
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import relationship


class Base(DeclarativeBase):
    pass


class Person(Base):
    __tablename__ = "person"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(32))
    fullname: Mapped[Optional[str]]
    password: Mapped[str] = mapped_column(String(256))


class Ability(Base):
    __tablename__ = "ability"
    id: Mapped[int] = mapped_column(primary_key=True)
    score: Mapped[int]
    modifier: Mapped[int]
    description: Mapped[str] = mapped_column(String(1024))


class Character(Base):
    __tablename__ = "character"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(32))
    # Hit Points
    hit_point_max: Mapped[int]
    hit_point_current: Mapped[int]

    age_id: Mapped[int] = mapped_column(ForeignKey("ability.id"))
    age: Mapped["Ability"] = relationship()

    strength_id: Mapped[int] = mapped_column(ForeignKey("ability.id"))
    strength: Mapped["Ability"] = relationship()

    dexterity_id: Mapped[int] = mapped_column(ForeignKey("ability.id"))
    dexterity: Mapped["Ability"] = relationship()

    constitution_id: Mapped[int] = mapped_column(ForeignKey("ability.id"))
    constitution: Mapped["Ability"] = relationship()

    intelligence_id: Mapped[int] = mapped_column(ForeignKey("ability.id"))
    intelligence: Mapped["Ability"] = relationship()

    wisdom_id: Mapped[int] = mapped_column(ForeignKey("ability.id"))
    wisdom: Mapped["Ability"] = relationship()

    charisma_id: Mapped[int] = mapped_column(ForeignKey("ability.id"))
    charisma: Mapped["Ability"] = relationship()

    person_id: Mapped[int] = mapped_column(ForeignKey("person.id"))
    person: Mapped["Person"] = relationship()

    background: Mapped[str] = mapped_column(String(1024))


def create_all_tables(engine):
    Base.metadata.create_all(engine)


def load_engine():
    engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)
    return engine
