#!/usr/bin/python3
"""this file contains code for testing the State class"""
import unittest
from models.engine.file_storage import FileStorage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.user import User


class Test_State(unittest.TestCase):
    """tests for the State class"""
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
        self.assertEqual(State, type(State()))

    def test_7(self):
        self.assertIn(State(), models.storage.all().values())

    def test_8(self):
        self.assertEqual(str, type(State().id))

    def test_9(self):
        self.assertEqual(datetime, type(State().created_at))

    def test_10(self):
        self.assertEqual(datetime, type(State().updated_at))
