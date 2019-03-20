from flask import current_app, jsonify
from flask import redirect
from flask import render_template
from flask import session
from person.models import User,Department

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

    # 从数据库获取用户数据
    try:
        users = User.query.all()
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg='查询管理员数据失败')
    # 判断查询结果
    if not users:
        return jsonify(errno=RET.NODATA, errmsg='无管理员数据')
    # 从数据库获取用户数据
    try:
        departments = Department.query.all()
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg='查询部门数据失败')
    # 判断查询结果
    if not departments:
        return jsonify(errno=RET.NODATA, errmsg='无部门数据')
    # 定义列表，存储部门数据
    department_list = []
    for department in departments:
        department_list.append(department)
    # 定义列表，存储用户数据
    users_list = []
    for user in users:
        users_list.append(user.to_dict())
    # 定义列表，存储数据
    data = {
        'users': users_list,
        'departments':department_list
    }
    return render_template('Admin.html', data=data)
