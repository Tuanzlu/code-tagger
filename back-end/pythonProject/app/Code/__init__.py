from flask import Blueprint

Code = Blueprint("Code", __name__)

from app.Code import routes
