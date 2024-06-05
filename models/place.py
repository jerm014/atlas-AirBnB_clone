#!/usr/bin/python3
"""this file contains code for the Place class"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    class for Place with attributes:
       * id         (BaseModel) (Primary Key)
       * updated_at (BaseModel)
       * created_at (BaseModel)
       * user_id                (Foreign Key to User)
       * name
       * city_id                (Foreign Key to City)
       * description
       * number_rooms
       * number_bathrooms
       * max_guest
       * price_by_night
       * latitude
       * longitude
    """

    user_id = ""
    name = ""
    city_id = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0.0
    latitude = 0.0
    longitude = 0.0
    amenities = list of Amenity
