from flask import render_template, redirect, url_for, request
from flask.views import MethodView
from pms.models import *
from pms.forms import EmployeeForm


class EmployeeListView(MethodView):
    def get(self, page=1):
        items = Employee.query.paginate(page, per_page=15)
        return render_template('emplist.html', employees=items)


class EmployeeDelView(MethodView):
    def get(self, id=None):
        if id:
            emp = db.session.query(Employee).get(id)
            if emp:
                db.session.delete(emp)
                db.session.commit()
        return redirect(url_for('admin.emp_list'))


class EmployeeAddView(MethodView):
    def get(self):
        departments = db.session.query(Department).all()
        return render_template('empadd.html', departments=departments)

    def post(self):
        employee = Employee(
            request.form.get('name'),
            request.form.get('gender', '男'),
            request.form.get('job'),
            datetime.strptime(request.form.get('birthdate'), '%Y-%m-%d'),
            request.form.get('idcard'),
            request.form.get('address'),
            float(request.form.get('salary'))
        )
        employee.department_id = int(request.form.get('department_id'))

        db.session.add(employee)
        db.session.commit()
        return redirect(url_for('.emp_list'))


class EmployeeAddOrEditView(MethodView):
    def get(self, id=None):
        # id为空时则新增用户 id不为空时为编辑用户
        # 创建Form表单时不要从数据库查询，如果内容是写死的可以直接写死
        # 如果数据需要从数据库查询，应该在构造实例之后，在呈现之前，否则得不到结果

        emp = Employee() if not id else db.session.query(Employee).get(id)  # get（主键）
        form = EmployeeForm(request.form, obj=emp)
        form.department_id.choices = [(d.id, d.name) for d in Department.query.all()]
        form.gender.choices = [('男', '男'), ('女', '女')]
        return render_template('empedit.html', form=form)

    def post(self, id=None):
        # 如果表单提交的数据包含id，则为编辑，否则为新增
        form = EmployeeForm(request.form)
        emp = Employee() if not id else db.session.query(Employee).get(id)  # get（主键）

        # 数据及表单能够一一对应，使用下面的方法直接嵌套
        form.populate_obj(emp)
        if not id:
            db.session.add(emp)
        db.session.commit()
        return redirect(url_for('.emp_list'))
