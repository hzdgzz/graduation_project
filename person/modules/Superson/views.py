from flask import session, render_template, current_app, jsonify, request, g
from . import Superson
# 导入模型类User
# from person.models import User, Category, News, Comment
# 导入自定义的状态码
from person.utils.response_code import RET
# 导入常量文件
from person import  db
# 导入自定义的登录验证装饰器
from person.utils.commons import login_required


@Superson.route("/")
# @login_required
def index():
    """

    :return:
    """
    # 一、用户信息展示
    # user = g.user

    return render_template('index.html')


# 管理员登录界面
@Superson.route("/AdminLogin.html")
def AdminLogin():
    return render_template('AdminLogin.html')

# 超级管理员操作页面
@Superson.route("/Supersons.html")
def Supersons():
    return render_template('Supersons.html')

# 管理员操作页面
@Superson.route("/Admin.html")
def Admin():
    return render_template('Admin.html')

