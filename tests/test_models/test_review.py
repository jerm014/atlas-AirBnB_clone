#!/usr/bin/python3
"""this file contains code for testing the Review class"""
import unittest
from models.engine.file_storage import FileStorage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.state import State
from models.user import User


class Test_Review(unittest.TestCase):
    """tests for the Review class"""
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
        self.assertEqual(Review, type(Review()))

    def test_7(self):
        self.assertIn(Review(), models.storage.all().values())

    def test_8(self):
        self.assertEqual(str, type(Review().id))

    def test_9(self):
        self.assertEqual(datetime, type(Review().created_at))
