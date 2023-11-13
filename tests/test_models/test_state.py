#!/usr/bin/python3
"""unittest for State"""
from models.state import State
import unittest


class Test_State(unittest.TestCase):
    """Test cases for State"""

    def test_name_is_public_str(self):
        self.assertEqual(str, type(State.name))
