from app.UserLabel import UserLabel

from flask import request, session, jsonify
from db.label_db import label_DB
from db.mark_db import mark_DB

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


@UserLabel.route('/')
def hello_world():
    return "hello AddLabel!"

@UserLabel.route('/addLabel', methods=["POST", "GET"])
def addUserLabel_func():
    if request.method == "GET":
        userId = request.args.get("userId")
        labelId = request.args.get("labelId")
        label = request.args.get("label")
    else:
        userId = request.form.get("userId")
        labelId = request.form.get("labelId")
        label = request.form.get("label")
    label1 = label_DB()
    rst = label1.oneUserAddLabel(userId, labelId, label)
    if rst == "existed":
        return jsonify({"state":'fail', "description": "Existing label", "moreMsg":rst})
    else:
        return jsonify({"state":'success', "description": "success", "moreMsg":rst})

@UserLabel.route('/getLabel', methods=["POST", "GET"])
def getLabel_func():
    if request.method == "GET":
        userId = request.args.get("userId")
        labelId = request.args.get("labelId")
    else:
        userId = request.form.get("userId")
        labelId = request.form.get("labelId")
    print(userId)
    label1 = label_DB()
    rst = label1.checkUserLabel(userId,labelId)
    return jsonify({'state':'success', "rst":rst})

@UserLabel.route('/getUser', methods=["POST", "GET"])
def getUserUser_func():
    if request.method == "GET":
        userId = request.args.get("userId")
        detail = request.args.get("detail")
    else:
        userId = request.form.get("userId")
        detail = request.form.get("detail")
    label1 = label_DB()
    if detail == False:
        rst = label1.selectOneUserlist(userId) 
    else:
        rst = label1.selectOneUserdetail(userId) 
    return jsonify({'state':'success', "rst":rst})


@UserLabel.route('/removeLabel', methods=["POST", "GET"])
def removeUserLabel_func():
    if request.method == "GET":
        userId = request.args.get("userId")
        labelId = request.args.get("labelId")
    else:
        userId = request.form.get("userId")
        labelId = request.form.get("labelId")
    label1 = label_DB()
    label1.oneUserRemoveLabel(userId, labelId)
    return jsonify({"state":'success', "description": "success"})

@UserLabel.route('/modifyLabelID', methods=["POST", "GET"])
def modifyLabelID_func():
    if request.method == "GET":
        userId = request.args.get("userId")
        labelId = request.args.get("labelId")
        labelId_new = request.args.get("labelId_new")
    else:
        userId = request.form.get("userId")
        labelId = request.form.get("labelId")
        labelId_new = request.form.get("labelId_new")
    label1 = label_DB()
    mark1 = mark_DB()
    rst = label1.checkUserLabel(userId,labelId_new)
    if rst == "existed":
        return jsonify({"state":'fail', "description": "Existing label"})
    else:
        label1.oneUserModifyLabelID(userId, labelId, labelId_new)
        mark1.oneUserModifyLabelID(userId, labelId, labelId_new)
        return jsonify({"state":'success', "description": "success"})

@UserLabel.route('/modifyLabelintro', methods=["POST", "GET"])
def modifyLabelintro_func():
    if request.method == "GET":
        userId = request.args.get("userId")
        labelId = request.args.get("labelId")
        label_new = request.args.get("label_new")
    else:
        userId = request.form.get("userId")
        labelId = request.form.get("labelId")
        label_new = request.form.get("label_new")
    label1 = label_DB()
    label1.oneUserModifyLabelintro(userId, labelId, label_new)
    return jsonify({"state":'success', "description": "success"})
