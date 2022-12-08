from flask import Flask 
from config import Config
from .models import db, User
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_moment import Moment 
from flask_cors import CORS

app = Flask(__name__)
# login = LoginManager()
moment = Moment(app)
CORS(app)

# @login.user.loader
# def load_user(user_id):
#     return User.query.get(user_id)

app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app, db)
# login.init_app(app)


from . import models
from . import routes