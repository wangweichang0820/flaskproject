import os
from flask import render_template, redirect, url_for, request
from filemanagement.models import *
from flask.views import MethodView

from flask import send_from_directory

# 上传文件目录
UPLOAD_FOLDER = r'.\uploads'
# 上传文件类型
ALLOWED_EXTENSIONS = ['.jpg', '.png', '.gif', '.psd', '.jpeg', '.txt', '.xls', '.xlsx']


# 检查文件是否允许上传
def allowed_file(filename):
    name, ext = os.path.splitext(filename)
    return ext.lower() in ALLOWED_EXTENSIONS


# # 文件下载
# @app.route('/download/<filename>', methods=['GET'])
# def download(filename):
#     path = UPLOAD_FOLDER + '/' + filename
#     print(path)
#     if os.path.exists(path):
#         return send_from_directory(UPLOAD_FOLDER, filename, as_attachment=True)
#     return '未找到文件'


class FileListView(MethodView):
    def get(self, page=1):
        items = File.query.paginate(page, per_page=15)
        return render_template('filelist.html', fileinfo=items)


class FileUploadView(MethodView):
    def get(self):
        return render_template('fileupload.html')

    def post(self):
        pass


class FileDownload(MethodView):
    def get(self):
        pass

    def post(self):
        pass
