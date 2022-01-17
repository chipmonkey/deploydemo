from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import os

__version__ = '1.0.0'

app = Flask(__name__, instance_relative_config=True)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv(
    "DATABASE_URL", "postgresql://demo:password@demo-postgres/demo"
)
# app.config.from_object(os.environ['APP_SETTINGS'])
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

db = SQLAlchemy(app)

# from models import Result
from chipchip import models

migrate = Migrate()
migrate.init_app(app, db)

try:
    os.makedirs(app.instance_path)
except OSError:
    pass

from chipchip.views import users
app.register_blueprint(users.bp)

