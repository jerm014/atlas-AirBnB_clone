#!/usr/bin/python3
"""this file contains code for the City class"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    class for City with attributes:
       * id         (BaseModel) (Primary Key)
       * updated_at (BaseModel)
       * created_at (BaseModel)
       * name
       * state_id               (Foreign Key to State)
    """

    name = ""
    state_id = ""
