from app.Mark import Mark

from flask import request, session, jsonify
from db.mark_db import mark_DB
from db.label_db import label_DB

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


@Mark.route('/')
def hello_world():
    return "hello Mark Code!"

@Mark.route('/addMark', methods=["POST", "GET"])
def addUserMark_func():
    if request.method == "GET":
        userId = request.args.get("userId")
        labelId = request.args.get("labelId")
        codeId = request.args.get("codeId")
        code = request.args.get("code")
        new = request.args.get("new")
    else:
        userId = request.form.get("userId")
        labelId = request.form.get("labelId")
        codeId = request.form.get("codeId")
        code = request.form.get("code")
        new = request.form.get("new")
    mark1 = mark_DB()
    label1 = label_DB()
    rst = mark1.oneUserAddMark(userId, codeId, code, labelId)
    if rst == "existed":
        return jsonify({"state":'fail', "description": "Existing mark", "moreMsg":rst})
    if new == False:
        return jsonify({"state":'success', "description": "success", "moreMsg":rst})
    else:
        rst2 = label1.oneUserAddLabel(userId, labelId, "")
        if rst2 == "existed":
            return jsonify({"state":'success', "description": "Existing label", "moreMsg":rst})
        else:
            return jsonify({"state":'success', "description": "success", "moreMsg":rst})

@Mark.route('/getLabelMark', methods=["POST", "GET"])
def getLabelMark_func():
    if request.method == "GET":
        userId = request.args.get("userId")
        labelId = request.args.get("labelId")
    else:
        userId = request.form.get("userId")
        labelId = request.form.get("labelId")
    print(userId)
    mark1 = mark_DB()
    rst = mark1.selectOneLabel(userId,labelId)
    return jsonify({'state':'success', "rst":rst})

@Mark.route('/getUserMark', methods=["POST", "GET"])
def getUserMark_func():
    if request.method == "GET":
        userId = request.args.get("userId")
    else:
        userId = request.form.get("userId")
    mark1 = mark_DB()
    rst = mark1.selectOneUser(userId)
    return jsonify({'state':'success', "rst":rst})

@Mark.route('/removeMark', methods=["POST", "GET"])
def removeUserMark_func():
    if request.method == "GET":
        userId = request.args.get("userId")
        labelId = request.args.get("labelId")
        codeId = request.args.get("codeId")
        code = request.args.get("code")
    else:
        userId = request.form.get("userId")
        labelId = request.form.get("labelId")
        codeId = request.form.get("codeId")
        code = request.form.get("code")
    mark1 = mark_DB()
    mark1.oneUserRemoveMark(userId, codeId, code, labelId)
    return jsonify({"state":'success', "description": "success"})




