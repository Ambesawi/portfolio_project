from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Configure the database connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@localhost/piyasa_dev_db'
db = SQLAlchemy(app)

# Define a User model for the database
class User(db.Model):
    UserID = db.Column(db.Integer, primary_key=True)
    First_name = db.Column(db.String(20), nullable=False)
    Last_Name = db.Column(db.String(20), nullable=False)
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
            new_user = User(First_name=first_name, Last_Name=last_name, Email=email, Password=hashed_password, Address=address, PhoneNumber=phone_number)
            db.session.add(new_user)
            db.session.commit()
            flash('Registration successful!', 'success')
    
    return redirect(url_for('index'))

# Handle contact us form submission and insert data into the database
@app.route('/contact', methods=['POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        # Insert the contact message into the database
        # You can create a ContactMessage model similar to User for this purpose
        # and store messages in a separate table

        flash('Message sent!', 'success')
    
    return redirect(url_for('index'))

# Handle login form submission and check user credentials in the database
@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check if a user with the provided username or email exists
        user = User.query.filter((User.Email == username) | (User.First_name == username)).first()

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
