import re

from flask import current_app
from flask import render_template, jsonify
from flask import request
from flask import session

from person.models import SuperAdmin
from person.utils.response_code import RET
from . import SuperadminLogin

@SuperadminLogin.route("/login", methods=['POST'])
def login():

    # 获取参数
    superadmin_id = request.json.get('superadmin_id')
    superadmin_password = request.json.get('superadmin_password')
    # superadmin_id = int(superadmin_id)
    # 检查参数的完整性
    if not all([superadmin_id, superadmin_password]):
        return jsonify(errno=RET.PARAMERR, errmsg='参数缺失')
    try:
        superadmin = SuperAdmin.query.filter_by(superadmin_id=superadmin_id).first()

    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DATAERR, errmsg='查询用户账号失败')
    try:
        superadmin_psw = SuperAdmin.query.filter_by(superadmin_psw=superadmin_password).first()
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DATAERR, errmsg='查询用户密码失败')
    if not superadmin or not superadmin_psw:
        return jsonify(errno=RET.PWDERR, errmsg='用户名或密码错误')
    # 实现状态保持
    session['superadmin_id'] = superadmin.superadmin_id
    session['superadmin_psw'] = superadmin.superadmin_psw
    return jsonify(errno=RET.OK, errmsg='OK')


# 超级管理员登录界面
@SuperadminLogin.route("/SuperadminLogin.html")
def SuperadminLogin():
    return render_template('SuperadminLogin.html')




