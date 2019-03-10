from flask import render_template
from . import SuperadminLogin
# 超级管理员登录界面
@SuperadminLogin.route("/SuperadminLogin.html")
def SuperadminLogin():
    return render_template('SuperadminLogin.html')