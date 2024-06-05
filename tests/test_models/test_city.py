#!/usr/bin/python3
"""this file contains code for testing the City class"""
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


class Test_City(unittest.TestCase):
    """tests for the City class"""
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
        self.assertEqual(City, type(City()))

    def test_7(self):
        self.assertIn(City(), models.storage.all().values())

    def test_8(self):
        self.assertEqual(str, type(City().id))

    def test_9(self):
        self.assertEqual(datetime, type(City().created_at))
