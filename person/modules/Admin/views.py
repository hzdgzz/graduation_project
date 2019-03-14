from flask import current_app, jsonify
from flask import render_template

from person.utils.response_code import RET
from . import Admin
# 超级管理员登录界面
@Admin.route("/Admin.html")
def Admin():

    return render_template('Admin.html')