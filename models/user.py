#!/usr/bin/python3
"""This module defines the User class for the AirBnB clone project."""
from models.base_model import BaseModel


class User(BaseModel):
    """Represents a User with email, password, first and last name."""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
