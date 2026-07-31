from flask import Blueprint, request, session
from sqlalchemy.exc import IntegrityError

from config import db
from models import User

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/signup", methods=["POST"])
def signup():
    data = request.get_json()

    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return {"error": "Username and password are required."}, 400

    user = User(username=username)
    user.password = password

    try:
        db.session.add(user)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return {"error": "Username already exists."}, 400

    session["user_id"] = user.id

    return {
        "id": user.id,
        "username": user.username,
    }, 201


@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    username = data.get("username")
    password = data.get("password")

    user = User.query.filter_by(username=username).first()

    if not user or not user.authenticate(password):
        return {"error": "Invalid username or password"}, 401

    session["user_id"] = user.id

    return {
        "id": user.id,
        "username": user.username,
    }, 200


@auth_bp.route("/me", methods=["GET"])
def me():
    user_id = session.get("user_id")

    if not user_id:
        return {
            "error": "Unauthorized"
        }, 401

    user = User.query.get(user_id)

    if not user:
        return {
            "error": "User not found"
        }, 404

    return {
        "id": user.id,
        "username": user.username
    }, 200


@auth_bp.route("/logout", methods=["DELETE"])
def logout():
    session.pop("user_id", None)
    return {}, 204