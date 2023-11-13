#!/usr/bin/python3
"""unittest for the Amenity"""
from models.amenity import Amenity
import unittest


class Test_Amenity(unittest.TestCase):
    """test cases for Amenity"""

    def test_name_is_public_str(self):
        self.assertEqual(str, type(Amenity.name))
