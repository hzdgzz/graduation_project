from flask import current_app
from flask import redirect
from flask import render_template, jsonify
from flask import session
from person.models import Department
from person.utils.response_code import RET
from . import Departments
# 退出登录
@Departments.route("/exit_department", methods=['POST'])
def exit_department():
    session.pop('admin_id', None)
    session.pop('admin_psw', None)
    print(session)
    return jsonify(errno='0', errmsg='OK')
# 部门界面
@Departments.route("/Department.html")
def Departments():
    try:
        # 获取用户状态保持信息
        superadmin_id = session['admin_id']
        superadmin_psw = session['admin_psw']
    except Exception as e:
        current_app.logger.error(e)
        return redirect('/')

    # 从数据库获取数据
    try:
        departments = Department.query.all()
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg='查询管理员数据失败')
    # 判断查询结果
    if not departments:
        return jsonify(errno=RET.NODATA, errmsg='无管理员数据')
    # 定义列表，存储数据
    data = {
        'departments': departments
    }
    return render_template('Department.html',data = data)
