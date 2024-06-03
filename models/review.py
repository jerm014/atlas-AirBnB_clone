#!/usr/bin/python3
"""this file contains code for the Review class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    class for Review with attributes:
       * id         (BaseModel) (Primary Key)
       * updated_at (BaseModel)
       * created_at (BaseModel)
       * user_id                (Foreign Key to User)
       * place_id               (Foreign Key to Place)
       * text
    """

    __user_id = None
    __place_id = None
    __text = ""

    @property
    def user_id(self):
        return self.__user_id

    @property
    def place_id(self):
        return self.__place_id

    @property
    def text(self):
        return self.__text

    @user_id.setter
    def user_id(self, value):
        self.__user_id = value

    @place_id.setter
    def place_id(self, value):
        self.__place_id = value

    @text.setter
    def text(self, value):
        self.__text = value
