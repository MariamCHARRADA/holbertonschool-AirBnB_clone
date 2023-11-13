#!/usr/bin/python3
"""unittest for the City"""
from models.city import City
import unittest


class Test_City(unittest.TestCase):
    """Test cases for City"""

    def test_state_id(self):
        self.assertEqual(str, type(City.state_id))

    def test_name(self):
        self.assertEqual(str, type(City.name))
