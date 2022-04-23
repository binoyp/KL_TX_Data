from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Enum

from ._base import Base
import enum


class LocalBodyType(enum.Enum):
    Corporation = 1
    GramaPanchayath = 2
    Muncipality = 3


class LocalBody(Base):
    __tablename__ = "localbodys"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    loc_type = Column(Enum(LocalBodyType))

    
