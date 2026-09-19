#!/usr/bin/python3
"""Unittest module for the State class."""
import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """Test cases for the State class."""

    def test_instance(self):
        """Test that State is an instance of BaseModel."""
        s = State()
        self.assertIsInstance(s, BaseModel)

    def test_name(self):
        """Test that name is empty string by default."""
        s = State()
        self.assertEqual(s.name, "")

    def test_class_doc(self):
        """Test that State class has a docstring."""
        self.assertIsNotNone(State.__doc__)


if __name__ == "__main__":
    unittest.main()
