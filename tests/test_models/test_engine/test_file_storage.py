#!/usr/bin/python3
"""this file contains code for testing the file stoage"""
import unittest
import models
from models.engine.file_storage import FileStorage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class Test_File_Storage(unittest.TestCase):
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
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_7(self):
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_8(self):
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def test_9(self):
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_a(self):
        self.assertEqual(type(models.storage), FileStorage)
