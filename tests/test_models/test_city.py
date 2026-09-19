#!/usr/bin/python3
"""Unittest module for the City class."""
import unittest
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """Test cases for the City class."""

    def test_instance(self):
        """Test that City is an instance of BaseModel."""
        c = City()
        self.assertIsInstance(c, BaseModel)

    def test_state_id(self):
        """Test that state_id is empty string by default."""
        c = City()
        self.assertEqual(c.state_id, "")

    def test_name(self):
        """Test that name is empty string by default."""
        c = City()
        self.assertEqual(c.name, "")

    def test_class_doc(self):
        """Test that City class has a docstring."""
        self.assertIsNotNone(City.__doc__)


if __name__ == "__main__":
    unittest.main()
