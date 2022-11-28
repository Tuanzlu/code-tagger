from flask import Blueprint

UserRepository = Blueprint("UserRepository", __name__)

from app.UserRepository import routes
