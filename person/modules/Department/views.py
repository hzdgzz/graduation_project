from flask import render_template
from . import Department
# 超级管理员登录界面
@Department.route("/Department.html")
def Department():
    return render_template('Department.html')