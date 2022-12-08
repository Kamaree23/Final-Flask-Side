from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash
from datetime import timezone, datetime
from flask_login import UserMixin
from secrets import token_hex

db = SQLAlchemy()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), nullable=False, unique=True)
    email = db.Column(db.String(50), nullable=False, unique=True)
    fname = db.Column(db.String(50), nullable=False, unique=True)
    lname = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(250), nullable=False)
    apitoken = db.Column(db.String, default=None, nullable=True)
    date_created = db.Column(db.DateTime, default=datetime.now(timezone.utc))

    def __init__(self, username, email, password, fname, lname):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)
        self.fname = fname
        self.lname = lname
        self.apitoken = token_hex(16)

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'token': self.apitoken
        }
    def saveToDB(self):
        db.session.add(self)
        db.session.commit()