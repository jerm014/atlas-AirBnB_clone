#!/usr/bin/python3
"""this file contains code for file storage"""
import json
from models.base_model import BaseModel
import os

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        self.__objects[obj.id] = obj.to_dict()

    def save(self):
        with open(self.__file_path, "w") as fileobj:
            json.dump(self.__objects, fileobj)

    def reload(self):
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, "r") as file:
                self.__objects = json.load(file)
            for key, value in self.__objects.items():
                self.__objects[key] = BaseModel(**value)
