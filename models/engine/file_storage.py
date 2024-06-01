#!/usr/bin/python3
"""this file contains code for file storage"""
import os
import json
from models.base_model import BaseModel

class FileStorage:
    __file_path = ""
    __objects = {}

    def __init__(self, file_path="file.json"):
        self.file_path = file_path
        self.objects = {}

    @property
    def file_path(self):
        return self.__file_path

    @property
    def objects(self):
        return self.__objects

    @file_path.setter
    def file_path(self, file_path):
        self.__file_path = file_path

    @objects.setter
    def objects(self, objects):
        self.__objects = objects

    def all(self):
        return self.objects

    def new(self, obj):
        self.objects[obj.id] = obj.to_dict()

    def save(self):
        with open(self.file_path, "w") as fileobj:
            json.dump(self.objects, fileobj)

    def reload(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, "r") as fileobj:
                for item in json.load(fileobj):
                    dictobj = {key: value for key, value in 
                                item.items() if key != '__class__'}
                    self.new(BaseModel(**dictobj))
