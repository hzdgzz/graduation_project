from flask import render_template
from . import AdminLogin
# 超级管理员登录界面
@AdminLogin.route("/AdminLogin.html")
def SuperadminLogin():
    return render_template('AdminLogin.html')