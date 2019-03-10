from flask import render_template
from . import Rewards
# 超级管理员登录界面
@Rewards.route("/Rewards.html")
def Rewards():
    return render_template('Rewards.html')