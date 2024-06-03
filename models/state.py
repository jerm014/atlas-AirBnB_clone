#!/usr/bin/python3
"""this file contains code for the State class"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    class for State with attributes:
        name
    """

    __name = ""

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value
