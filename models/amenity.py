#!/usr/bin/python3
"""this file contains code for the Amenity class"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    class for Amenity with attributes:
       * id         (BaseModel) (Primary Key)
       * updated_at (BaseModel)
       * created_at (BaseModel)
       * name
    """

    __name = ""

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value
