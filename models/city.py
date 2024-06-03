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

    __name = ""
    __state_id = None

    @property
    def name(self):
        return self.__name

    @property
    def state_id(self):
        return self.__state_id

    @name.setter
    def name(self, value):
        self.__name = value

    @state_id.setter
    def state_id(self, value):
        self.__state_id = value
