import re

from flask import current_app
from flask import redirect
from flask import render_template, jsonify
from flask import request
from flask import session

from person import db
from person.models import RewardsPunishment, User
from person.utils.response_code import RET
from . import Rewards


# 添加奖惩数据
@Rewards.route("/add_userreward", methods=['POST'])
def add_admindepartment():
    # 获取参数
    auser_id = request.json.get('auser_id')
    auser_name = request.json.get('auser_name')
    auser_tel = request.json.get('auser_tel')
    auser_reward = request.json.get('auser_reward')
    auser_punish = request.json.get('auser_punish')
    # 检查参数的完整性
    if not all([auser_id, auser_name, auser_tel, auser_reward, auser_punish]):
        return jsonify(errno=RET.PARAMERR, errmsg='参数缺失')
    # 校验是否int类型
    try:
        auser_id = int(auser_id)
        auser_reward = int(auser_reward)
        auser_punish = int(auser_punish)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.PARAMERR, errmsg='参数类型错误')
    # 检查手机号
    if not re.match(r'1[3456789]\d{9}$', auser_tel):
        return jsonify(errno=RET.PARAMERR, errmsg='手机号格式错误')
    # 根据id查询用户
    try:
        user = User.query.filter_by(user_id=auser_id).first()
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.PARAMERR, errmsg='此用户不存在错误')
    try:
        user.user_name = auser_name
        user.user_mobile = auser_tel
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DATAERR, errmsg='要新增的用户姓名或手机号错误')
    # 构建模型类对象
    rewardspunishment = RewardsPunishment()
    rewardspunishment.user_id = auser_id
    rewardspunishment.reward = auser_reward
    rewardspunishment.punishment = auser_punish
    # 存入数据库
    try:
        db.session.add(rewardspunishment)
        db.session.commit()
    except Exception as e:
        current_app.logger.error(e)
        db.session.rollback()
        return jsonify(errno=RET.DBERR, errmsg='保存数据失败')
        # 返回前端数据
    return jsonify(errno='0', errmsg='OK')
# 编辑员工数据
@Rewards.route("/editor_userreward", methods=['PUT'])
def editor_userreward():
    # 获取参数
    userId = request.json.get('userId')
    euser_id = request.json.get('euser_id')
    euser_reward = request.json.get('euser_reward')
    euser_punish = request.json.get('euser_punish')
    # 检查参数的完整性
    if not all([userId, euser_id,euser_reward, euser_punish]):
        return jsonify(errno=RET.PARAMERR, errmsg='参数缺失')
    # 校验是否int类型
    try:
        userId = int(userId)
        euser_id = int(euser_id)
        euser_reward = int(euser_reward)
        euser_punish = int(euser_punish)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.PARAMERR, errmsg='参数类型错误')
    # 检查要删除的对象和输入的是否一致
    if userId!=euser_id:
        return jsonify(errno=RET.DATAERR, errmsg='要编辑的员工和输入的不一致错误')
    # 构建模型类对象
    try:
        rewardspunishment = RewardsPunishment.query.filter_by(user_id=euser_id).first()
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg='查询奖惩员工错误')
    rewardspunishment.user_id = euser_id
    rewardspunishment.reward = euser_reward
    rewardspunishment.punishment = euser_punish
    # 存入数据库
    try:
        db.session.add(rewardspunishment)
        db.session.commit()
    except Exception as e:
        current_app.logger.error(e)
        db.session.rollback()
        return jsonify(errno=RET.DBERR, errmsg='保存数据失败')
        # 返回前端数据
    return jsonify(errno=RET.OK, errmsg='OK')

# 删除员工奖励
@Rewards.route("/delete_userreward", methods=['DELETE'])
def delete_userreward():
    # 获取参数
    userId = request.json.get('userId')
    euser_id = request.json.get('euser_id')
    # 检查参数的完整性
    if not all([userId, euser_id]):
        return jsonify(errno=RET.PARAMERR, errmsg='参数缺失')
    # 校验是否int类型
    try:
        userId = int(userId)
        euser_id = int(euser_id)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.PARAMERR, errmsg='参数类型错误')

    # 检查用户输入id和列表id是否一致
    if userId != euser_id:
        return jsonify(errno=RET.DATAERR, errmsg='请输入正确要删除的员工id')
    # 构建模型类对象
    try:
        rewards = RewardsPunishment.query.filter_by(user_id=euser_id).first()
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg='查询员工数据错误')
    rewards.is_deleted = 1
    # 存入数据库
    try:
        db.session.add(rewards)
        db.session.commit()
    except Exception as e:
        current_app.logger.error(e)
        db.session.rollback()
        return jsonify(errno=RET.DBERR, errmsg='删除员工数据失败')
        # 返回前端数据
    return jsonify(errno='0', errmsg='OK')

# 退出登录
@Rewards.route("/exit_rewards", methods=['POST'])
def exit_rewards():
    session.pop('admin_id', None)
    session.pop('admin_psw', None)
    print(session)
    return jsonify(errno='0', errmsg='OK')


# 奖惩界面
@Rewards.route("/Rewards.html")
def Rewards():
    try:
        # 获取用户状态保持信息
        superadmin_id = session['admin_id']
        superadmin_psw = session['admin_psw']
    except Exception as e:
        current_app.logger.error(e)
        return redirect('/')
    # 从数据库获取数据
    try:
        rewardspunishments = RewardsPunishment.query.all()

    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg='查询管理员数据失败')

    # 判断查询结果
    if not rewardspunishments:
        return jsonify(errno=RET.NODATA, errmsg='无管理员数据')
    # 定义列表，存储数据
    data = []
    for rewardspunishment in rewardspunishments:
        data.append(rewardspunishment.to_dict())
    return render_template('Rewards.html', data=data)
