#!/usr/bin/python3
"""this file contains code for file storage"""
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage:
    __file_path = ""
    __objects= []

    def all(self):
        pass

    def new(self, obj):
        pass

    def save(self):
        pass

    def reload(self):
        pass
