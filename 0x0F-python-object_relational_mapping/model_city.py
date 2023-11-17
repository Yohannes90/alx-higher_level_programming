#!/usr/bin/python3

""" module that contains city class
"""
from model_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """ class representation of city
    """
    __tablename__ = 'cities'
    id = Column(Integer(), autoincrement=True,
                nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer(), ForeignKey("state.id"), nullable=False)
