#!/usr/bin/python3
""" holds class User"""

import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from hashlib import md5


class User(BaseModel, Base):
    """Representation of a user """
    if models.storage_t == 'db':
        __tablename__ = 'users'
        UserID = Column(INT(20), nullable=False)
        FirstName = Column(CHAR(20), nullable=False)
        LastName = Column(CHAR(20), nullable=False)
        Email = Column(VARCHAR(45), nullable=False)
        Password = Column(VARCHAR(45), nullable=False)
	Address = Column(VARCHAR(45), nullable=False)
	PhoneNumber = Column(INT(45), nullable=False)
        orders = relationship("Order", backref="user")
    else:
        Email = ""
        Password = ""
        FirstName = ""
        LastName = ""

    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)

    def __setattr__(self, name, value):
        """sets a password with md5 encryption"""
        if name == "Password":
            value = md5(value.encode()).hexdigest()
        super().__setattr__(name, value)
