#!/usr/bin/python3
"""this file contains code for testing the Amenity class"""
import unittest
import models
from models.engine.file_storage import FileStorage
from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class Test_Amenity(unittest.TestCase):
    """tests for the Amenity class"""
    def test_1(self):
        pass
    
    def test_2(self):
        pass

    def test_3(self):
        pass

    def test_4(self):
        pass

    def test_5(self):
        pass

    def test_6(self):
        self.assertEqual(Amenity, type(Amenity()))

    def test_7(self):
        self.assertIn(Amenity(), models.storage.all().values())

    def test_8(self):
        self.assertEqual(str, type(Amenity().id))

    def test_9(self):
        self.assertEqual(datetime, type(Amenity().created_at))

