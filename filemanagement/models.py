from datetime import datetime
from app import db


class User(db.Model):
    '''员工信息'''
    __tablename__ = 'userinfo'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))  # 用户名
    password = db.Column(db.String(255))  # 密码
    realname = db.Column(db.String(255))  # 真实名称
    gender = db.Column(db.String(16))  # 性别
    birthdate = db.Column(db.Date)  # 出生年月
    address = db.Column(db.String(255))  # 地址
    email = db.Column(db.String(64))  # 邮箱
    cellphone = db.Column(db.String(64))  # 手机号码
    workunit = db.Column(db.String(255))  # 工作单位
    profession = db.Column(db.String(255))  # 工作行业
    status = db.Column(db.Integer)  # 状态
    registertime = db.Column(db.DateTime)  # 注册时间

    def __init__(self, username=None, password=None, realname=None, gender=None, birthdate=None, address=None,
                 email=None, cellphone=None, workunit=None, profession=None, status=1, registertime=None):
        self.username = username
        self.password = password
        self.realname = realname
        self.gender = gender
        self.address = address
        self.birthdate = birthdate
        self.email = email
        self.cellphone = cellphone
        self.status = status
        self.workunit = workunit
        self.profession = profession
        self.registertime = registertime if registertime else datetime.now()

    def __repr__(self):
        return '<用户{}：{}{}{}>'.format(self.id, self.username, self.realname, self.address)


class File(db.Model):
    '''员工信息'''
    __tablename__ = 'fileinfo'

    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(255))
    savename = db.Column(db.String(64))
    extensionname = db.Column(db.String(16))
    filesize = db.Column(db.Integer)
    file_category = db.Column(db.String(255))
    uploadtime = db.Column(db.DateTime)
    savepath = db.Column(db.String(255))

    # 创建外键
    uploaduser_id = db.Column(db.Integer, db.ForeignKey('userinfo.id'))
    # 与Department 创建关联
    uploadusername = db.relationship('User', backref=db.backref('fileinfo', lazy='dynamic'))

    def __init__(self, filename=None, savename=None, extensionname=None, filesize=0, file_category=None, savepath=None,
                 uploadtime=None):
        self.filename = filename
        self.savename = savename
        self.extensionname = extensionname
        self.filesize = filesize
        self.file_category = file_category
        self.savepath = savepath
        self.uploadtime = uploadtime if uploadtime else datetime.now()

    def __repr__(self):
        return '<文件{}：{}{}{}>'.format(self.id, self.filename, self.file_category, self.savepath)
