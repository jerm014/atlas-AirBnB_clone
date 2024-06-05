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

    email = ""
    first_name = ""
    last_name = ""
    password = ""
