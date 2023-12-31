#!/usr/bin/python3
"""unittest for the Place"""
from models.place import Place
import unittest


class Test_Place(unittest.TestCase):
    """Test cases for Place"""

    def test_city_id(self):
        self.assertEqual(str, type(Place.city_id))

    def test_name(self):
        self.assertEqual(str, type(Place.name))

    def test_number_rooms(self):
        self.assertEqual(str, type(Place.number_rooms))

    def test_latitude(self):
        self.assertEqual(float, type(Place.latitude))

    def test_amenity_ids(self):
        self.assertEqual(list, type(Place.amenity_ids))
