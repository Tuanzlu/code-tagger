from flask import Blueprint

Mark = Blueprint("Mark", __name__)

from app.Mark import routes
