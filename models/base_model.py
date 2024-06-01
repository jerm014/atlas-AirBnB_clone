#!/usr/bin/python3
"""this file contains code for the BaseModel class"""
import uuid
from datetime import datetime
import models


class BaseModel:
    def __init__(self, *args, **kwargs):
        """init the object"""
        now = datetime.now()
        self.id = str(uuid.uuid4())
        self.created_at = now
        self.updated_at = now
        if kwargs:
            for key, value in kwargs.items():
                if key.endswith("_at"):
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
            if "id" not in kwargs:
                self.id = str(uuid.uuid4())
                self.created_at = self.updated_at = datetime.now()

    def __str__(self):
        """print out the string representation of the object"""
        res = "[{}] ".format(self.__class__.__name__)
        res += "({}) ".format(self.id) + str(BaseModel.to_dict(self))
        return (res)

    def to_dict(self):
        """return this as a dictionary objet"""
        d = self.__dict__.copy()
        d["__class__"] = self.__class__.__name__
        d["created_at"] = self.created_at.isoformat()
        d["updated_at"] = self.updated_at.isoformat()
        return d

    def save(self):
        """Update updated_at"""
        self.updated_at = datetime.now()
        storage.save(self)

    @staticmethod
    def get_last_three_letters(a_list):
        return ''.join([x[-3:].lower() for x in a_list if len(x) > 2])
