from . import db

class Department(db.Model):
    """部门"""

    __tablename__ = "department"
    depart_id = db.Column(db.Integer, unique=True,primary_key=True)  # 部门编号
    depart_name = db.Column(db.String(32), unique=True, nullable=False)  # 部门名称
    User = db.relationship("Uesr", backref='department', lazy="dynamic")
    # repr()方法显示一个可读字符串
    def __repr__(self):
        return 'Role:%s' % self.name



class User(db.Model):
    """员工"""

    __tablename__ = "user"
    user_id = db.Column(db.Integer, unique=True,primary_key=True)  # 员工编号
    user_name = db.Column(db.String(32), nullable=False)  # 员工姓名
    user_age = db.Column(db.Integer)  # 员工年龄
    user_gender = db.Column(
        db.Enum(
            "MAN",  # 男
            "WOMAN"  # 女
        ),
        default="MAN")  # 员工性别
    depart_id = db.Column(db.Integer, db.ForeignKey('department.depart_id'))  # 部门编号
    user_mobile = db.Column(db.String(11), unique=True, nullable=False)  # 员工手机号
    user_email = db.Column(db.String(11), unique=True, nullable=False)  # 员工邮箱
    rewardspunishment = db.relationship("RewardsPunishment", backref='user', lazy="dynamic")


    # repr()方法显示一个可读字符串
    def __repr__(self):
        return 'Role:%s' % self.name


class Recruiter(db.Model):
    """招聘人员"""

    __tablename__ = "Recruiter"
    recruiter_id = db.Column(db.Integer, unique=True,primary_key=True)  # 招聘编号
    recruiter_name = db.Column(db.String(32), nullable=False)  # 招聘姓名
    recruiter_age = db.Column(db.Integer)  # 招聘年龄
    recruiter_gender = db.Column(
        db.Enum(
            "MAN",  # 男
            "WOMAN"  # 女
        ),
        default="MAN")  # 招聘性别
    recruiter_mobile = db.Column(db.String(11), unique=True, nullable=False)  # 招聘手机号
    recruiter_email = db.Column(db.String(11), unique=True, nullable=False)  # 招聘邮箱


    # repr()方法显示一个可读字符串
    def __repr__(self):
        return 'Role:%s' % self.name


class Admin(db.Model):
    """管理员"""

    __tablename__ = "admin"
    admin_id = db.Column(db.Integer, unique=True,primary_key=True)  # 管理员编号
    admin_psw = db.Column(db.String(32), nullable=False)  # 管理员密码


    # repr()方法显示一个可读字符串
    def __repr__(self):
        return 'Role:%s' % self.name


class SuperAdmin(db.Model):
    """超级管理员"""

    __tablename__ = "superadmin"
    superadmin_id = db.Column(db.Integer, unique=True,primary_key=True)  # 超级管理员编号
    superadmin_psw = db.Column(db.String(32), nullable=False)  # 超级管理员密码


    # repr()方法显示一个可读字符串
    def __repr__(self):
        return 'Role:%s' % self.name


class RewardsPunishment(db.Model):
    """奖惩"""

    __tablename__ = "rewardspunishment"

    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'),primary_key=True)  # 员工编号
    user_name = db.Column(db.Integer, db.ForeignKey('user.user_name'))  # 员工姓名
    user_mobile = db.Column(db.Integer, db.ForeignKey('user.user_mobile'))  # 员工电话
    reward = db.Column(db.Integer)  # 员工奖励
    punishment = db.Column(db.Integer)  # 员工惩罚


    # repr()方法显示一个可读字符串
    def __repr__(self):
        return 'Role:%s' % self.name


