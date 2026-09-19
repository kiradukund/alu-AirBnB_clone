#!/usr/bin/python3
"""Unittest module for the Review class."""
import unittest
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """Test cases for the Review class."""

    def test_instance(self):
        """Test that Review is an instance of BaseModel."""
        r = Review()
        self.assertIsInstance(r, BaseModel)

    def test_place_id(self):
        """Test that place_id is empty string by default."""
        r = Review()
        self.assertEqual(r.place_id, "")

    def test_user_id(self):
        """Test that user_id is empty string by default."""
        r = Review()
        self.assertEqual(r.user_id, "")

    def test_text(self):
        """Test that text is empty string by default."""
        r = Review()
        self.assertEqual(r.text, "")

    def test_class_doc(self):
        """Test that Review class has a docstring."""
        self.assertIsNotNone(Review.__doc__)


if __name__ == "__main__":
    unittest.main()
