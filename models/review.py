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

    user_id = ""
    place_id = ""
    text = ""
