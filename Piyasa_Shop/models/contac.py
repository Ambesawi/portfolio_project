from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Contact(db.Model):
    ContactID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(20), nullable=False)
    Email = db.Column(db.String(20), nullable=False)
    Message = db.Column(db.Text, nullable=False)

    def __init__(self, name, email, message):
        self.Name = name
        self.Email = email
        self.Message = message
