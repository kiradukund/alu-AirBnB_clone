#!/usr/bin/python3
"""Unittest module for the Amenity class."""
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """Test cases for the Amenity class."""

    def test_instance(self):
        """Test that Amenity is an instance of BaseModel."""
        a = Amenity()
        self.assertIsInstance(a, BaseModel)

    def test_name(self):
        """Test that name is empty string by default."""
        a = Amenity()
        self.assertEqual(a.name, "")

    def test_class_doc(self):
        """Test that Amenity class has a docstring."""
        self.assertIsNotNone(Amenity.__doc__)


if __name__ == "__main__":
    unittest.main()
