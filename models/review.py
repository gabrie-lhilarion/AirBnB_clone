#!/usr/bin/python3
"""
Review class, a subclass of BaseModel class
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    A subclass of BaseModel class
    Public class attributes:
        place_id:             
        user_id:              
        text:                 
    """
    place_id = ""
    user_id = ""
    text = ""