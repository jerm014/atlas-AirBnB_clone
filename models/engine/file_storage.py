#!/usr/bin/python3
"""this file contains code for file storage"""
import json
from models.base_model import BaseModel
import os
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

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
    classes = {"Amenity": Amenity,
               "BaseModel": BaseModel,
               "City": City,
               "Place": Place,
               "Review": Review,
               "State": State,
               "User": User}

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
        try:
            with open(self.__file_path, 'r') as f:
                new_object_dict = json.load(f)
            for k, v in new_object_dict.items():
                obj = self.classes[value['__class__']](**v)
                self.__objects[k] = obj
        except FileNotFoundError:
            pass

    @property
    def file_path(self):
        return self.__file_path

    @file_path.setter
    def file_path(self, value):
        self.__file_path = value
