#!/usr/bin/python3
"""this file contains code for the Place class"""
from models.base_model import BaseModel


class Place(BaseModel):
    def to_dictionary(self):
        """return a dictionary describing the Place"""
        d = {"id": self.id,
             "updated_at": self.updated_at,
             "created_at": self.created_at,
             "name": self.name}
        return d
