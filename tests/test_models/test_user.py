#!/usr/bin/python3
"""unittest for the User"""
from models.user import User
import unittest


class Test_User(unittest.TestCase):
    """Test cases for User"""

    def test_email_is_public_str(self):
        self.assertEqual(str, type(User.email))

    def test_password_is_public_str(self):
        self.assertEqual(str, type(User.password))

    def test_first_name_is_public_str(self):
        self.assertEqual(str, type(User.first_name))

    def test_last_name_is_public(self):
        self.assertEqual(str, type(User.last_name))
