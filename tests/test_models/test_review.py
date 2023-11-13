#!/usr/bin/python3
"""unittest for the review"""
from models.review import Review
from datetime import datetime
import unittest
import uuid


class Test_Review(unittest.TestCase):
    """Test cases for Review"""

    def test_place_id(self):
        self.assertEqual(str, type(Review.place_id))

    def test_user_id(self):
        self.assertEqual(str, type(Review.user_id))

    def test_text(self):
        self.assertEqual(str, type(Review.text))
