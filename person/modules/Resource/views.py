from flask import current_app
from flask import redirect
from flask import render_template, jsonify
from flask import session

from . import Resource

# 退出登录
@Resource.route("/exit_resource", methods=['POST'])
def exit_resource():
    session.pop('admin_id', None)
    session.pop('admin_psw', None)
    print(session)
    return jsonify(errno='0', errmsg='OK')
# 超级管理员登录界面
@Resource.route("/Resource.html")
def Resource():
    try:
        # 获取用户状态保持信息
        superadmin_id = session['admin_id']
        superadmin_psw = session['admin_psw']
    except Exception as e:
        current_app.logger.error(e)
        return redirect('/')
    return render_template('Resource.html')