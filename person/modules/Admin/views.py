from flask import current_app, jsonify
from flask import redirect
from flask import render_template
from flask import session
from person.models import User

from person.utils.response_code import RET
from . import Admin


@Admin.route("/exit_admin", methods=['POST'])
def exit_admin():
    session.pop('admin_id', None)
    session.pop('admin_psw', None)
    print(session)
    return jsonify(errno='0', errmsg='OK')


# 超级管理员登录界面
@Admin.route("/Admin.html")
def Admin():
    try:
        # 获取用户状态保持信息
        superadmin_id = session['admin_id']
        superadmin_psw = session['admin_psw']
    except Exception as e:
        current_app.logger.error(e)
        return redirect('/')

    # 从数据库获取数据
    try:
        users = User.query.all()
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg='查询管理员数据失败')
    # 判断查询结果
    if not users:
        return jsonify(errno=RET.NODATA, errmsg='无管理员数据')
    # 定义列表，存储数据
    data = {
        'users': users
    }
    return render_template('Admin.html', data=data)
