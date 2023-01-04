from app.Code import Code

from flask import request, session, jsonify
from db.code_db import code_DB


codeDB = code_DB()


# 两个函数，用于将flask_sql的输出转化为可以直接网络传输的json格式
# 用法：直接调用classlist2dictlist，输入可以是单个object或者多个object的列表
def class2dict(class_entry):
    ret = {}
    remove_keys = ['_sa_instance_state']
    for e in class_entry.__dict__:
        if e in remove_keys:
            continue
        ret[e] = class_entry.__dict__[e]
    return ret


def classlist2dictlist(class_entries):
    if type(class_entries) != type([]):
        class_entries = [class_entries]
    ret_list = [class2dict(e) for e in class_entries]
    return ret_list


@Code.route('/')
def hello_world():
    return "hello to AddCodeFile!"


@Code.route('/addCode', methods=['POST', "GET"])
def addUserCode():
    if request.method == "GET":
        userId = request.args.get("userId")
        codeId = request.args.get("codeId")
        code = request.args.get("code")
    else:
        userId = request.form.get("userId")
        codeId = request.form.get("codeId")
        code = request.args.get("code")
    rst = codeDB.oneUserAddCode(userId, codeId, code)
    return jsonify({"state":'success', "description": "success", "moreMsg":rst})


@Code.route('/getCode', methods=["POST", "GET"])
def getUserCode():
    if request.method == "GET":
        userId = request.args.get("userId")
    else:
        userId = request.form.get("userId")
    print(userId)
    rst = codeDB.selectOneUser(userId)
    return jsonify({'state':'success', "rst":rst})


@Code.route('/removeCode', methods=["POST", "GET"])
def removeUserCode():
    if request.method == "GET":
        userId = request.args.get("userId")
        codeId = request.args.get("codeId")
        code = request.args.get("code")
    else:
        userId = request.form.get("userId")
        codeId = request.form.get("codeId")
        code = request.args.get("code")
    codeDB.oneUserRemoveLabel(userId, codeId, code)
    return jsonify({"state":'success', "description": "success"})

@Code.route('/modifyCodeID', methods=["POST", "GET"])
def modifyCodeID():
    if request.method == "GET":
        userId = request.args.get("userId")
        codeId = request.args.get("codeId")
        codeID_new = request.args.get("codeId_new")
    else:
        userId = request.form.get("userId")
        codeId = request.form.get("codeId")
        codeID_new = request.args.get("codeId_new")
    codeDB.oneUserModifyCodeID(userId, codeId, codeID_new)
    return jsonify({"state":'success', "description": "success"})

@Code.route('/modifyCode', methods=["POST", "GET"])
def modifyCode():
    if request.method == "GET":
        userId = request.args.get("userId")
        codeId = request.args.get("codeId")
        code_new = request.args.get("code_new")
    else:
        userId = request.form.get("userId")
        codeId = request.form.get("codeId")
        code_new = request.args.get("code_new")
    codeDB.oneUserModifyLabelintro(userId, codeId, code_new)
    return jsonify({"state":'success', "description": "success"})
