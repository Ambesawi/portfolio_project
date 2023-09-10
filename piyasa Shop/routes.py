# Import Flask
from os import environ
from flask import Flask, render_template

# Create a Flask app
app = Flask(__name__)

# Route for the homepage
@app.route('/')
def index():
    # Fetch data and pass it to the template as needed
    # Example data:
    products = ["Product 1", "Product 2", "Product 3"]
    return render_template('index.html', products=products, page_title="Pyasa Fashion")

# Route for the contact us page
@app.route('/contact-us')
def contact_us():
    return render_template('contact_us.html', page_title="Contact Us")

# Route for the registration page
@app.route('/register')
def register():
    return render_template('register.html', page_title="Register")

# Route for the login page
@app.route('/login')
def login():
    return render_template('login.html', page_title="Login")

# Route for other static pages (e.g., /mens, /womens, /kids, /explore)
@app.route('/<page>')
def static_page(page):
    # You can customize this function to serve different static pages
    # based on the 'page' argument.
    return render_template(f'index.html', page_title=page.capitalize())

if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000, debug=False)

