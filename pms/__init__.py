from flask import Blueprint

admin = Blueprint('admin', __name__)
from pms.views import *

# 防止视图重复造成冲突
emp_list_view = EmployeeListView.as_view('emp_list')

admin.add_url_rule('/emp/list/', view_func=emp_list_view, defaults={'page': 1})  # 首页，不带页码
admin.add_url_rule('/emp/list/<int:page>/', view_func=emp_list_view)  # 其他页，带页码

admin.add_url_rule('/emp/del/<int:id>/', view_func=EmployeeDelView.as_view('emp_del'))
admin.add_url_rule('/emp/add/', view_func=EmployeeAddView.as_view('emp_add'))
admin.add_url_rule('/emp/add<int:id>/', view_func=EmployeeAddOrEditView.as_view('emp_edit'))
