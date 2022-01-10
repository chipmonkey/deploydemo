"""
Do a thing
"""

from demo import app, db

from demo.models import User
from flask import request, redirect, jsonify


@app.route("/")
def hello():
    """ Hello World
    """
    return "Hello World!"


@app.route("/say/<name>")
def hello_name(name):
    """ Hello name
    """
    return f"Hello {name}!"


@app.route("/user/<userid>", methods=["GET"])
def user_userid(userid):
    """
    Get it
    """
    result = User.query.filter_by(id=userid).first()

    # return f"Get User {userid} from db"
    return jsonify(result.serialize)


@app.route("/user/", methods=["POST"])
@app.route("/user", methods=["POST"])
def adduser():
    """
    Post User
    """
    name = request.json.get("name")
    if not name:
        return redirect("/")

    user = User(name=name)
    db.session.add(user)
    db.session.commit()
    return request.json


@app.route("/userx/", methods=["PATCH"])
@app.route("/userx", methods=["PATCH"])
def patchuser():
    """
    Patch User
    """
    return request.json


@app.route("/user/<int:userid>", methods=["POST"])
def updateuser(userid):
    """
    Update User
    """
    return "Update User {userid} from db".format(userid)
