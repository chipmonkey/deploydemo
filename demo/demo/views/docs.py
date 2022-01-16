from flask import Flask, jsonify
from flask_swagger import swagger

from demo import app

@app.route("/docs")
def spec():
    return jsonify(swagger(app))
