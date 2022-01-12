from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import os

__version__ = '0.0.1'

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv(
    "DATABASE_URL", "postgresql://demo:password@demo-postgres/demo"
)
# app.config.from_object(os.environ['APP_SETTINGS'])
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
db = SQLAlchemy(app)

# from models import Result
from demo import models

migrate = Migrate()
migrate.init_app(app, db)


import demo.views

if __name__ == "__main__":
    app.run()
