#!/usr/bin/python3
"""unittest for State"""
from models.state import State
import unittest
from datetime import datetime
import uuid


class Test_User(unittest.TestCase):
    """Class Test for State"""

    def test_name_is_public_str(self):
        self.assertEqual(str, type(State.name))
