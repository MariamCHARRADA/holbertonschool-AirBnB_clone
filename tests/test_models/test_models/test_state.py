#!/usr/bin/python3
"""unittest for State"""

from models.base_model import BaseModel
from models.state import State
import unittest
import datetime


class Test_State(unittest.TestCase):
    """Class Test for State"""

    def test_name_is_public_str(self):
        self.assertEqual(str, type(State.name))
