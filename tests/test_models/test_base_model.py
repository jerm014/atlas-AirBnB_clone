#!/usr/bin/python3
"""this file contains code for testing the BaseModel class"""
import unittest
import models
from datetime import datetime
from models.engine.file_storage import FileStorage
from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class Test_BaseModel(unittest.TestCase):
    """tests for the BaseModel class"""
    def test_1(self):
        b = BaseModel()
        initial_modify_at = b.updated_at
        b.save()
        self.assertNotEqual(initial_modify_at, b.updated_at)
    
    def test_2(self):
        pass

    def test_3(self):
        pass

    def test_4(self):
        pass

    def test_5(self):
        pass
