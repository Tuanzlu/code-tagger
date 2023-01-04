from app.User import User
from flask import request, session, jsonify, render_template
from db.user_db import user_DB


user = user_DB()


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
    info = ''
    telphone = request.form.get("telphone")
    password = request.form.get("password")
    res = user.GetLoginInfo(telphone)
    if res == None:
        info = '无用户信息，请注册'
        #return render_template('index.html', info=info)
        return '无用户信息，请注册'
    temp = list(res.values())
    res_p = temp[0]
    if res_p == password:
        info = '登录成功'
        session['telphone'] = telphone
        #return render_template('index.html', info=info)
        return '登录成功'
    else:
        info = '登录失败'
        #return render_template('index.html', info=info)
        return '登录失败'


    return render_template('index.html', info='Unknow Error!!!')


@User.route('/register', methods=['POST'])
def register():
    info = ''
    username = request.form.get("username")
    telphone = request.form.get("telphone")
    password = request.form.get("password")
    password_again = request.form.get("password_again")
    res = user.GetSameTelphone(telphone)
    res_username = user.GetSameUsername(username)
    if res:
        info = '手机号已被使用，请更换手机号重试'
        #return render_template('index.html', info=info)
        return '手机号已被使用，请更换手机号重试'
    if res_username:
        info = '用户名已被使用，请更换用户名重试'
        # return render_template('index.html', info=info)
        return '用户名已被使用，请更换用户名重试'
    if password != password_again:
        info = '两次密码不一致'
        #return render_template('index.html', info=info)
        return '两次密码不一致'
    else:
        info = '注册成功'
        user.addUser(username, password, telphone)
        # return jsonify({"state": 'success', "description": "success"})
        # return render_template('index.html', info=info)
        return '注册成功'

    return render_template('index.html', info='Unknow Error!!!')


@User.route('/exit', methods=['GET'])
def exit():
    info = ''
    res = session.get('telphone')
    if res == None:
        info = '未登录'
        #return render_template('index.html', info=info)
        return '未登录'
    else:
        session['telphone'] = None
        info = '账号已成功注销'
        #return render_template('index.html', info=info)
        return '账号已成功注销'

    return render_template('index.html', info='Unknow Error!!!')

@User.route('/removeUser', methods=["POST", "GET"])
def removeUser():
    info = ''
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
        info = '输入信息有误，删除失败'
        #return render_template('index.html', info=info)
        return '输入信息有误，删除失败'
    else:
        info = '删除成功'
        user.removeUser(username, password, telphone)
        # return render_template('index.html', info=info)
        # return jsonify({"state":'success', "description": "success"})
        return '删除成功'

    return render_template('index.html', info='Unknow Error!!!')
