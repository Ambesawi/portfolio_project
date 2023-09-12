#!/usr/bin/python3
""" holds class User"""

import models
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from hashlib import md5
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Define your MySQL database connection parameters
db_config = {
    "host": "localhost",
    "user": "your_username",
    "password": "your_password",
    "database": "piyasa_dev_db",  # Your database name
}

# Configure the database connection
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql://{db_config['user']}:{db_config['password']}@{db_config['host']}/{db_config['database']}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Create the database object
db = SQLAlchemy(app)

# Define a User model for the database
class User(db.Model):
    UserID = db.Column(db.Integer, primary_key=True)
    FirstName = db.Column(db.String(20), nullable=False)
    LastName = db.Column(db.String(20), nullable=False)
    Email = db.Column(db.String(45), unique=True, nullable=False)
    Password = db.Column(db.String(45), nullable=False)
    Address = db.Column(db.String(45), nullable=False)
    PhoneNumber = db.Column(db.Integer, nullable=False)

# Handle registration form submission and insert data into the database
@app.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        first_name = request.form['firstName']
        last_name = request.form['lastName']
        email = request.form['email']
        password = request.form['password']
        address = request.form['address']
        phone_number = request.form['phoneNumber']

        # Check if the email is already registered
        if User.query.filter_by(Email=email).first():
            flash('Email already registered!', 'error')
        else:
            # Hash the password before storing it in the database
            hashed_password = generate_password_hash(password, method='sha256')
            
            # Create a new user instance and add it to the database
            new_user = User(FirstName=first_name, LastName=last_name, Email=email, Password=hashed_password, Address=address, PhoneNumber=phone_number)
            db.session.add(new_user)
            db.session.commit()
            flash('Registration successful!', 'success')
    
    return redirect(url_for('index'))

# Handle login form submission and check user credentials in the database
@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check if a user with the provided username or email exists
        user = User.query.filter((User.Email == username) | (User.FirstName == username)).first()

        if user and check_password_hash(user.Password, password):
            flash('Login successful!', 'success')
            # Redirect to the profile page upon successful login
            return redirect(url_for('profile'))

        flash('Invalid username or password. Please try again.', 'error')

    return redirect(url_for('index'))

# Define the profile route to display the profile.html page
@app.route('/profile')
def profile():
    return render_template('profile.html')

# Define the main index route
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
