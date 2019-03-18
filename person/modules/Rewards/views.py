from flask import current_app
from flask import redirect
from flask import render_template, jsonify
from flask import session

from . import Rewards

# 退出登录
@Rewards.route("/exit_rewards", methods=['POST'])
def exit_rewards():
    session.pop('admin_id', None)
    session.pop('admin_psw', None)
    print(session)
    return jsonify(errno='0', errmsg='OK')
# 超级管理员登录界面
@Rewards.route("/Rewards.html")
def Rewards():
    try:
        # 获取用户状态保持信息
        superadmin_id = session['admin_id']
        superadmin_psw = session['admin_psw']
    except Exception as e:
        current_app.logger.error(e)
        return redirect('/')
    return render_template('Rewards.html')