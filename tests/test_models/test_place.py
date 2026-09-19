#!/usr/bin/python3
"""Unittest module for the Place class."""
import unittest
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """Test cases for the Place class."""

    def test_instance(self):
        """Test that Place is an instance of BaseModel."""
        p = Place()
        self.assertIsInstance(p, BaseModel)

    def test_city_id(self):
        """Test that city_id is empty string by default."""
        p = Place()
        self.assertEqual(p.city_id, "")

    def test_user_id(self):
        """Test that user_id is empty string by default."""
        p = Place()
        self.assertEqual(p.user_id, "")

    def test_name(self):
        """Test that name is empty string by default."""
        p = Place()
        self.assertEqual(p.name, "")

    def test_number_rooms(self):
        """Test that number_rooms is 0 by default."""
        p = Place()
        self.assertEqual(p.number_rooms, 0)

    def test_class_doc(self):
        """Test that Place class has a docstring."""
        self.assertIsNotNone(Place.__doc__)


if __name__ == "__main__":
    unittest.main()
