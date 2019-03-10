from flask import render_template
from . import Admin
# 超级管理员登录界面
@Admin.route("/Admin.html")
def SuperadminLogin():
    return render_template('Admin.html')