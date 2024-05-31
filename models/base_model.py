#!/usr/bin/python3
"""this file contains code for the BaseModel class"""
import uuid
from datetime import datetime


class BaseModel:
    def __init__(self):
        now = datetime.now()
        self.id = str(uuid.uuid4())
        self.created_at = now
        self.updated_at = now

    def __str__(self):
        print("[{}] ({}) {}", self.__name__, self.id, self.to_dictionary())
