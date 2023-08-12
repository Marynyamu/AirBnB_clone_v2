#!/usr/usr/bin/python3
"""The module inherit from BaseModule"""

from models.base_model import BaseModel


class City(BaseModel):
    """The class for city"""

    state_id = ""
    name = ""
