from flask import Blueprint

UserLabel = Blueprint("UserLabel", __name__)

from app.UserLabel import routes
