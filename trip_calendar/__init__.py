# from TakeHome import models
from flask import Flask
from config import Config
from .api.routes import api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from trip_calendar.models import db as root_db, ma
from flask_marshmallow import Marshmallow
from flask_cors import CORS
# from .helpers import JSONEncoder

app = Flask(__name__)


app.register_blueprint(api)

app.config.from_object(Config)

root_db.init_app(app)

migrate = Migrate(app, root_db)

# ma.init_app(app)

# app.json_encoder = JSONEncoder

# CORS(app)
