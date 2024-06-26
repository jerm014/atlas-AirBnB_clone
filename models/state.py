#!/usr/bin/python3
"""this file contains code for the State class"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    class for State with attributes:
       * id         (BaseModel) (Primary Key)
       * updated_at (BaseModel)
       * created_at (BaseModel)
       * name
    """

    name = ""
