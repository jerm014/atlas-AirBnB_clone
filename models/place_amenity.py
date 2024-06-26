#!/usr/bin/python3
"""this file contains code for the PlaceAmenity class"""
from models.base_model import BaseModel


class PlaceAmenity(BaseModel):
    """
    class for PlaceAmenity with attributes:
       * id         (BaseModel) (Primary Key)
       * updated_at (BaseModel)
       * created_at (BaseModel)
       * amenity_id             (Foreign Key to Amenity)                    
       * place_id               (Foreign Key to Place)

    this should be called AmenityPlace and it should have an id and updatd_at
    and created_at in the model but again, I didn't make the rules for this
    """

    amenity_id = ""
    place_id = ""
