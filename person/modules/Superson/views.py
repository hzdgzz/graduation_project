from flask import current_app, jsonify
from flask import render_template

from person.utils.response_code import RET
from . import Superson
from person.models import Admin


@Superson.route("/")
def index():
    return render_template('index.html')


@Superson.route("/Supersons.html")
def Supersons():
    # 从数据库获取数据
    try:
        admins = Admin.query.all()
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg='查询管理员数据失败')
    # 判断查询结果
    if not admins:
        return jsonify(errno=RET.NODATA, errmsg='无管理员数据')
    # 定义列表，存储数据
    data = {
        'admins':admins
    }
    return render_template('Supersons.html', data=data)
