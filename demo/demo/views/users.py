"""
Do a thing
"""

from demo import app, db


from demo.models import User
from flask import request, redirect, jsonify, abort


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
def get_user_by_userid(userid):
    """
    Get it
    """
    result = User.query.filter_by(id=userid).first()
    db.session.remove()

    return jsonify(result.serialize)

@app.route("/users/", methods=["GET"])
def get_users():
    """
    Get them all
    """
    result = User.query.order_by(User.id).all()

    return jsonify([x.serialize for x in result])


@app.route("/user/", methods=["POST"])
@app.route("/user", methods=["POST"])
@app.route("/v1/user/", methods=["POST"])
@app.route("/v1/user", methods=["POST"])
def adduser():
    """
    Post User
    """
    name = request.json.get("name")
    if not name:
        abort(404)

    user = User(name=name)
    db.session.add(user)
    db.session.commit()
    return request.json

@app.route("/v2/user/", methods=["POST"])
@app.route("/v2/user", methods=["POST"])
def v2_adduser():
    """
    Post User with first and last name
    """
    first = request.json.get("first")
    last = request.json.get("last")
    if not first or not last:
        abort(404)

    user = User.init_v2(first=first, last=last)
    db.session.add(user)
    db.session.commit()
    return request.json



@app.route("/user/", methods=["PATCH"])
@app.route("/user", methods=["PATCH"])
@app.route("/v1/user/", methods=["PATCH"])
@app.route("/v1/user", methods=["PATCH"])
def patchuser():
    """
    Patch User to update name
    """
    name = request.json.get("name")
    if not name:
        abort(404)

    userid = request.json.get("userid")
    if not userid:
        abort(404)

    user = User.query.filter_by(id=userid).first()
    user.name = name
    db.session.commit()
    return request.json


@app.route("/v2/user/", methods=["PATCH"])
@app.route("/v2/user", methods=["PATCH"])
def v2_patchuser():
    """
    Update user with first and last name
    """
    first = request.json.get("first")
    last = request.json.get("last")
    userid = request.json.get("userid")

    if not first:
        abort(404)
    if not last:
        abort(404)
    if not userid:
        abort(404)

    user = User.query.filter_by(id=userid).first()
    user.first = first
    user.last = last
    db.session.commit()
    return request.json
