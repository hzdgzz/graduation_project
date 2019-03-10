import re

from flask import current_app
from flask import render_template, jsonify
from flask import request

from person.models import SuperAdmin
from person.utils.response_code import RET
from . import SuperadminLogin

@SuperadminLogin.route("/login", methods=['POST'])
def login():
    # 获取参数
    mobile = request.json.get('mobile')
    password = request.json.get('password')
    # 检查参数的完整性
    if not all([mobile, password]):
        return jsonify(errno=RET.PARAMERR, errmsg='参数缺失')

    return jsonify(errno=RET.OK, errmsg='用户名或密码错误')


# 超级管理员登录界面
@SuperadminLogin.route("/SuperadminLogin.html")
def SuperadminLogin():
    return render_template('SuperadminLogin.html')




