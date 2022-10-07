from flask_wtf import Form
import wtforms


class EmployeeForm(Form):
    # 创建Form表单时不要从数据库查询，如果内容是写死的可以直接写死
    # 如果数据需要从数据库查询，应该在构造实例之后，在呈现之前，否则得不到结果
    name = wtforms.StringField('姓名')
    gender = wtforms.RadioField('性别', default='男')
    job = wtforms.StringField('职位', default='工程师')
    birthdate = wtforms.DateField('生日')
    idcard = wtforms.StringField('身份证号')
    address = wtforms.StringField('地址')
    salary = wtforms.DecimalField('工资')

    # department = wtforms.SelectField('部门', choices=[(1, '财务部'), (2, '技术部'), (3, '市场部')])
    department_id = wtforms.SelectField('部门')
