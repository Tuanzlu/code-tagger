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
    data = []
    for n in rst:
        temp = list(n.values())
        name = temp[0]
        mnum = markDB.getnumRelation(name)
        cnum = codeDB.getnumFile(name)
        lnum = labelDB.getnumTag(name)
        tel = list(userDB.Gettelphone(name).values())[0]
        data.append({"username":name, "telphone":tel, "numFile":cnum, "numTag":lnum, "numRelation":mnum})
    return jsonify(data)

@Admin.route('/removeUser', methods=["POST", "GET"])
def removeUser():
    if request.method == "GET":
        userId = str(request.args.get("userId"))
        adminpassword = request.args.get("adminpassword")
    else:
        userId = str(request.form.get("userId"))
        adminpassword = request.form.get("adminpassword")
    res = userDB.GetAdminPassword()
    temp = list(res.values())
    res_p = temp[0]
    if adminpassword != res_p:
        return jsonify({"state": 'fail', "description": "Wrong password"})
    else:
        userDB.admin_removeUser(userId)
        markDB.admin_removeUser(userId)
        labelDB.admin_removeUser(userId)
        codeDB.admin_removeUser(userId)
        return jsonify({"state":'success', "description": "success"})
