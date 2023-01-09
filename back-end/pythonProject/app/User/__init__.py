from flask import Blueprint, jsonify

User = Blueprint("User", __name__)

from app.User import routes

from db.user_db import user_DB

user = user_DB()

res = user.GetSameUsername('admin')
if res == None:
    user.addUser('admin', '123456', '11111111111')
