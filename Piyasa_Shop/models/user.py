#!/usr/bin/python3
""" holds class User"""

import models
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from hashlib import md5
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(db.Model):
    UserID = db.Column(db.Integer, primary_key=True)
    FirstName = db.Column(db.String(20), nullable=False)
    LastName = db.Column(db.String(20), nullable=False)
    Email = db.Column(db.String(45), unique=True, nullable=False)
    Password = db.Column(db.String(45), nullable=False)
    Address = db.Column(db.String(45), nullable=False)
    PhoneNumber = db.Column(db.Integer, nullable=False)

    def __init__(self, first_name, last_name, email, password, address, phone_number):
        self.FirstName = first_name
        self.LastName = last_name
        self.Email = email
        self.Password = generate_password_hash(password, method='sha256')  # Hash the password before storing it
        self.Address = address
        self.PhoneNumber = phone_number

    def check_password(self, password):
        return check_password_hash(self.Password, password)
