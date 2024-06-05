#!/usr/bin/python3
"""this file contains code for testing the User class"""
import unittest
from models.engine.file_storage import FileStorage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class Test_User(unittest.TestCase):
    """tests for the User class"""
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
        self.assertEqual(User, type(User()))

    def test_7(self):
        self.assertIn(User(), models.storage.all().values())

    def test_8(self):
        self.assertEqual(str, type(User().id))

    def test_9(self):
        self.assertEqual(datetime, type(User().created_at))

    def test_a(self):
        self.assertEqual(datetime, type(User().updated_at))

    def test_b(self):
        self.assertEqual(str, type(User.email))

    def test_c(self):
        self.assertEqual(str, type(User.password))

    def test_d(self):
        self.assertEqual(str, type(User.first_name))

    def test_e(self):
        self.assertEqual(str, type(User.last_name))
