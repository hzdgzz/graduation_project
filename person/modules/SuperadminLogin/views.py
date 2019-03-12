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
    superadmin_id = request.json.get('superadmin_id')
    password = request.json.get('password')
    # superadmin_id = int(superadmin_id)
    # 检查参数的完整性
    if not all([superadmin_id, password]):
        return jsonify(errno=RET.PARAMERR, errmsg='参数缺失')
    try:
        user = SuperAdmin.query.filter_by(superadmin_id=superadmin_id).first()
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DATAERR, errmsg='账号错误')

    return jsonify(errno=RET.OK, errmsg='用户名或密码错误')


# 超级管理员登录界面
@SuperadminLogin.route("/SuperadminLogin.html")
def SuperadminLogin():
    return render_template('SuperadminLogin.html')




