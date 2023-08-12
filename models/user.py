#!/usr/bin/python3
"""The module for user"""

from models.base_model import BaseModel


class User(BaseModel):
    """The class is inheriting from BaseModel"""

    
    email = ""
    password = ""
    last_name = ""
    first_name = ""
