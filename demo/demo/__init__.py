"""
Initialize me!
"""

import os

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv(
    "DATABASE_URL", "postgresql://demo:password@demo-postgres/demo"
)
# app.config.from_object(os.environ['APP_SETTINGS'])
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
db = SQLAlchemy(app)

from demo import models  # pylint: disable=wrong-import-position

migrate = Migrate()
migrate.init_app(app, db)


from demo.views import users  # pylint: disable=wrong-import-position
from demo.views import docs  # pylint: disable=wrong-import-position
