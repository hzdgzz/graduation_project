from flask import current_app
from flask import redirect
from flask import render_template, jsonify
from flask import session

from . import Department
# 退出登录
@Department.route("/exit_department", methods=['POST'])
def exit_department():
    session.pop('admin_id', None)
    session.pop('admin_psw', None)
    print(session)
    return jsonify(errno='0', errmsg='OK')
# 部门界面
@Department.route("/Department.html")
def Department():
    try:
        # 获取用户状态保持信息
        superadmin_id = session['admin_id']
        superadmin_psw = session['admin_psw']
    except Exception as e:
        current_app.logger.error(e)
        return redirect('/')
    return render_template('Department.html')
