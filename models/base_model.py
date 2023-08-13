#!/usr/bin/python3
"""This module defines a base class
for all models in our hbnb clone
"""

import uuid
from datetime import datetime
import models


class BaseModel:
    """A base class
    for all hbnb models
    """

    def __init__(self, *args, **kwargs):
        """checks if their is
        keyword argument or otherwise
        """

        if not kwargs:
            self.id = (uuid.uuid4())
            self.updated_at = datetime.now()
            self.created_at = datetime.now()
        else:
            for k in kwargs:
                if k in ['created_at', 'updated_at']:
                    setattr(self, k, datetime.fromisoformat(kwargs[k]))
                elif k != '__class__':
                    setattr(self, k, kwargs[k])

    def __str__(self):
        """it return a string
        representation of an instance
        """

        clsName = self.__class__.__name__
        return "[{}] ({}) {}".format(clsName, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with
        current time when instance is changed
        """

        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Convert instance
        into dict format
        """

        dct = self.__dict__.copy()
        dct.update({
            "__class__": self.__class__.__name__,
            "updated_at": self.updated_at.isoformat(),
            "created_at": self.created_at.isoformat()
            })
        return dct
