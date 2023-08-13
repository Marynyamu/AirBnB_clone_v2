#!/bin/usr/bin/python3
"""The module inherit from BaseModel"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Is the class for user reviews"""

    place_id = ""
    user_id = ""
    text = ""
