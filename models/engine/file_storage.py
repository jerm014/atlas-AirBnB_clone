#!/usr/bin/python3
"""this file contains code for file storage"""
import json
from models.base_model import BaseModel
import os

class FileStorage:
    """
        class for FileStorage, with attributes:
          * file_path
          * objects
        
        methods:
          * all       - return the objects saved
          * new       - save a new object to the objects saved
          * save      - write the objects to JSON located at file_path
          * reload    - reload the objects from JSON located at file_path
          * file_path - getter and setter for file_path

        attributes:
          * file_path - the path to the file for JSON to be saved/reloaded
          * objects   - the objects that are being or have been saved
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):

        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """
        serialize obj dictionaries to JSON
        the file is specified in file_path
        """
        obj_dict = {}

        for key, obj in self.__objects.items():
            obj_dict[key] = obj.to_dict()

        with open(self.file_path, 'w') as f:
            json.dump(obj_dict, f)

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
