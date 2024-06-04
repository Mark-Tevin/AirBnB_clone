#!/usr/bin/python3
"""
This module creates a City class.
"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    Class for managing cities.

    Attributes:
        state_id (str): The ID of the state the city belongs to.
        name (str): The name of the city.
    """
    state_id = ""
    name = ""
