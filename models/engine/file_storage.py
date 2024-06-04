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
        """
        serializes objects in self.__objects to JSON and save in the file
        specified by __file_path
        """

        objects_dictionary = {}
        with open(self.file_path, "w") as fileobj:
            for key, value in self.__objects.items():
                objects_dictionary[key] = value.to_dict()
            json.dump(objects_dictionary, fileobj)

    def reload(self):
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, "r") as file:
                self.__objects = json.load(file)
            for key, value in self.__objects.items():
                self.__objects[key] = BaseModel(**value)

    @property
    def file_path(self):
        return self.__file_path

    @file_path.setter
    def file_path(self, value):
        self.__file_path = value
