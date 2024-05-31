#!/usr/bin/python3
"""this file contains code for the City class"""
from models.base_model import BaseModel


class City(BaseModel):
    def to_dictionary(self):
        """return a dictionary describing the City"""
        d = {"id": self.id,
             "updated_at": self.updated_at,
             "created_at": self.created_at,
             "state_id": self.state_id,
             "name": self.name}
        return d
