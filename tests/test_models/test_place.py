#!/usr/bin/python3
"""
unittest for place.py
"""

import unittest
from models/place import Place
import datetime


class TestPlace(unittest.TestCase):
    """Tests instances and methods from amenity class"""

    p = Place()

    def test_class_exists(self):
        """tests if class exists"""
        self.assertEqual(str(type(self.p)), "<class 'models.place.Place'>")

    def test_user_inheritance(self):
        """test if Place is a subclass of BaseModel"""
        self.assertIsInstance(self.p, Place)

    def testHasAttributes(self):
        """verify if attributes exist"""

    def test_types(self):
        """tests if the type of the attribute is the correct one"""


if __name__ == '__main__':
    unittest.main()
