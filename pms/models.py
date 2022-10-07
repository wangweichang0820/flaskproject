from datetime import datetime
from app import db


class Department(db.Model):
    '''    部门信息   '''
    __tablename__ = 'department'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)

    def __init__(self, name):
        self.name = name

    def __repr__(self, ):
        return '<部门> {}:{}'.format(self.id, self.name)


class Employee(db.Model):
    '''员工信息'''
    __tablename__ = 'employee'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
    gender = db.Column(db.String(10))
    job = db.Column(db.String(64))
    birthdate = db.Column(db.DateTime)
    idcard = db.Column(db.String(32))
    address = db.Column(db.String(255))
    salary = db.Column(db.Float)
    release_time = db.Column(db.DateTime)
    # 创建外键
    department_id = db.Column(db.Integer, db.ForeignKey('department.id'))
    # 与Department 创建关联
    department = db.relationship('Department', backref=db.backref('employees', lazy='dynamic'))

    def __init__(self, name=None, gender=None, job=None, birthdate=None, idcard=None, address=None, salary=0.00,
                 release_time=None):
        self.name = name
        self.gender = gender
        self.job = job
        self.birthdate = birthdate
        self.idcard = idcard
        self.address = address
        self.salary = salary
        self.release_time = release_time if release_time else datetime.now()



    def __repr__(self):
        return '<员工{}：{}{}{}>'.format(self.id, self.name, self.salary, self.address)
