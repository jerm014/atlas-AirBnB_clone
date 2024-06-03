#!/usr/bin/python3
"""this file contains code for the User class"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    class for User with attributes:
       * id         (BaseModel) (Primary Key)
       * updated_at (BaseModel)
       * created_at (BaseModel)
       * email
       * first_name
       * last_name
       * password

    password is stored as an MD5 digest,
    which was declared unsably broken in 1996.
    """

    __email = ""
    __first_name = ""
    __last_name = ""
    __password = ""

    @property
    def email(self):
        return self.__email

    @property
    def password(self):
        return self.__password

    @property
    def first_name(self):
        return self.__first_name

    @property
    def last_name(self):
        return self.__last_name

    @email.setter
    def email(self, value):
        self.__email = value

    @password.setter
    def password(self, value):
        self.__password = value

    @first_name.setter
    def first_name(self,value):
        self.__first_name = value

    @last_name.setter
    def last_name(self, value):
        self.__last_name = value
