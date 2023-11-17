#!/usr/bin/python3

""" module that contains state class
"""
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base

myMetaData = MetaData()
Base = declarative_base(metadata=myMetaData)


class State(Base):
    """ class representation of state
    """
    __tablename__ = 'states'
    id = Column(Integer(), autoincrement=True,
                nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
