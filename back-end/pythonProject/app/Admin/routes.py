from app.Admin import Admin

from flask import request, session, jsonify
from db.code_db import code_DB
from db.mark_db import mark_DB
from db.user_db import user_DB
from db.label_db import label_DB

codeDB = code_DB()
markDB = mark_DB()
userDB = user_DB()
labelDB = label_DB()

@Admin.route('/')
def hello_world():
    return "hello to Admin!"


@Admin.route('/getUsers', methods=["POST", "GET"])
def getUser():
    rst = userDB.selectAllUserlist()
    return jsonify({'state':'success', "rst":rst})

@Admin.route('/removeUser', methods=["POST", "GET"])
def removeUser():
    if request.method == "GET":
        userId = str(request.args.get("userId"))
    else:
        userId = str(request.form.get("userId"))
    userDB.admin_removeUser(userId)
    markDB.admin_removeUser(userId)
    labelDB.admin_removeUser(userId)
    codeDB.admin_removeUser(userId)
    return jsonify({"state":'success', "description": "success"})
