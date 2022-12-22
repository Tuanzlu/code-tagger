from flask import Blueprint

User = Blueprint("User", __name__)

from app.User import routes
