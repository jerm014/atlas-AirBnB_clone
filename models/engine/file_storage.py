#!/usr/bin/python3
"""this file contains code for file storage"""
import json
import models

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
        try:
            with open(FileStorage.__file_path, encoding="UTF8") as fd:
                FileStorage.__objects = json.load(fd)
            for key, value in FileStorage.__objects.items():
                class_name = value["__class__"]
                class_name = models.classes[class_name]
                FileStorage.__objects[key] = class_name(**value)
        except FileNotFoundError:
            pass
