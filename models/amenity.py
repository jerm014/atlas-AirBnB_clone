#!/usr/bin/python3
"""this file contains code for the Amenity class"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    def to_dictionary(self):
        """return a dictionary describing the Amenity"""
        d = {"id": self.id,
             "updated_at": self.updated_at,
             "created_at": self.created_at,
             "name": self.name}
        return d
