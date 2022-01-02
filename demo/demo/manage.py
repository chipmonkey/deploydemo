import os

from flask.cli import FlaskGroup
from demo import app, db

# app.config.from_object(os.environ['APP_SETTINGS'])

cli = FlaskGroup(app)


if __name__ == '__main__':
    cli()
