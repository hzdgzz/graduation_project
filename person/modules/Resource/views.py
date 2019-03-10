from flask import render_template
from . import Resource
# 超级管理员登录界面
@Resource.route("/Resource.html")
def Resource():
    return render_template('Resource.html')