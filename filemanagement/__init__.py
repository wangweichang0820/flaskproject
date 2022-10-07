from flask import Blueprint

filemaneger = Blueprint('filemaneger', __name__)
from filemanagement.views import *

# 防止视图重复造成冲突
file_list_view = FileListView.as_view('file_list')

filemaneger.add_url_rule('/list/', view_func=file_list_view, defaults={'page': 1})  # 首页，不带页码
filemaneger.add_url_rule('/list/<int:page>/', view_func=file_list_view)  # 其他页，带页码

filemaneger.add_url_rule('/upload/', view_func=FileUploadView.as_view('file_upload'))