#!/usr/bin/python3
"""this file contains code for the BaseModel class"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """Base Model class, parent to other classes."""

    __created_at = datetime.now()
    __updated_at = datetime.now()
    __id = ""

    def __init__(self, *args, **kwargs):
        """initialize this object, set properties"""
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
                self.created_at = now
                self.updated_at = now

    def __str__(self):
        """print out the string representation of the object"""
        res = "[{}] ".format(self.__class__.__name__)
        res += "({}) ".format(self.id) + str(BaseModel.to_dict(self))
        return (res)

    def to_dict(self):
        """return self as a dictionary objet"""
        d = self.__dict__.copy()
        d["__class__"] = self.__class__.__name__
        d["created_at"] = self.created_at.isoformat()
        d["updated_at"] = self.updated_at.isoformat()
        return d

    def save(self):
        """update updated_at and save the data using storage"""
        self.updated_at = datetime.now()
        models.storage.save()

    @property
    def id(self):
        return self.__id

    @property
    def created_at(self):
        return self.__created_at

    @property
    def updated_at(self):
        return self.__updated_at

    @id.setter
    def id(self, value):
        self.__id = value

    @created_at.setter
    def created_at(self, value):
        self.__created_at = value

    @updated_at.setter
    def updated_at(self,value):
        self.__updated_at = value
