from app.User import User
from flask import request, session, jsonify, render_template
from db.user_db import user_DB
from db.code_db import code_DB


user = user_DB()
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


@User.route('/')
def hello_world():
    return "hello to Login!"


@User.route('/login', methods=['POST'])
def login():
    telphone = request.form.get("telphone")
    password = request.form.get("password")
    res = user.GetLoginInfo(telphone)
    if res == None:
        return jsonify({"state":'fail', "description": "No user information, please sign up"})
    temp = list(res.values())
    res_p = temp[0]
    if res_p == password:
        session['telphone'] = telphone
        rst = user.GetUsername(telphone)
        return jsonify({'state': 'success', "rst": rst})

    else:
        return jsonify({"state":'fail', "description": "Wrong password"})


@User.route('/register', methods=['POST'])
def register():
    username = request.form.get("username")
    telphone = request.form.get("telphone")
    password = request.form.get("password")
    password_again = request.form.get("password_again")
    res = user.GetSameTelphone(telphone)
    res_username = user.GetSameUsername(username)
    if res:
        return jsonify({"state":'fail', "description": "The telephone number has been used, please change the telephone number and try again"})
    if res_username:
        return jsonify({"state":'fail', "description": "The username has been used, please change the username and try again"})
    if password != password_again:
        return jsonify({"state":'fail', "description": "The two passwords do not match"})
    else:
        user.addUser(username, password, telphone)
        return jsonify({"state":'success', "description": "success"})


@User.route('/exit', methods=['GET'])
def exit():
    res = session.get('telphone')
    if res == None:
        return jsonify({"state":'fail', "description": "Not logged in"})
    else:
        session['telphone'] = None
        return jsonify({"state":'success', "description": "success"})


@User.route('/removeUser', methods=["POST", "GET"])
def removeUser():
    if request.method == "GET":
        username = request.args.get("username")
        telphone = request.args.get("telphone")
        password = request.args.get("password")
    else:
        username = request.form.get("username")
        telphone = request.form.get("telphone")
        password = request.form.get("password")
    res = user.checkUser(username, password, telphone)
    if res == None:
        return jsonify({"state": 'fail', "description": "The input information is wrong, delete failed"})
    else:
        user.removeUser(username, password, telphone)
        codeDB.removeOneUser(username)
        return jsonify({"state":'success', "description": "success"})


@User.route('/modifyPassword', methods=['POST'])
def modifyPassword():
    telphone = request.form.get("telphone")
    old_password = request.form.get("old_password")
    new_password = request.form.get("new_password")
    new_password_again = request.form.get("new_password_again")
    res = user.GetLoginInfo(telphone)
    if res == None:
        return jsonify({"state":'fail', "description": "Please enter the correct telephone"})
    temp = list(res.values())
    res_p = temp[0]
    if res_p != old_password:
        return jsonify({"state":'fail', "description": "Please enter the correct old password"})
    else:
        if new_password == old_password:
            return jsonify({"state": 'fail', "description": "Please enter a new password different from the old one"})
        elif new_password != new_password_again:
            return jsonify({"state":'fail', "description": "The two passwords do not match"})
        else:
            user.updatePassword(telphone, new_password)
            return jsonify({"state":'success', "description": "success"})


@User.route('/getUserlist', methods=['POST'])
def getUserlist():
    adminpassword = request.form.get("adminpassword")
    res = user.GetAdminPassword()
    temp = list(res.values())
    res_p = temp[0]
    if adminpassword != res_p:
        return jsonify({"state":'fail', "description": "Wrong password"})
    else:
        rst = user.selectAllUser()
        return jsonify({'state': 'success', "rst": rst})


@User.route('/admin_removeUser', methods=['POST'])
def admin_removeUser():
    adminpassword = request.form.get("adminpassword")
    username = request.form.get("username")
    res = user.GetAdminPassword()
    temp = list(res.values())
    res_p = temp[0]
    if adminpassword != res_p:
        return jsonify({"state": 'fail', "description": "Wrong password"})
    else:
        user.removeUser(username)
        return jsonify({"state":'success', "description": "success"})
