from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


# 解决静态资源无法加载问题
app = Flask(__name__, static_url_path='')

# 配置 SECRET_KEY
app.config["SECRET_KEY"] = "1169097790@qq.com"

# 数据库配置信息
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:123456@localhost/pms"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config['SQLALCHEMY_ECHO'] = True
# 创建数据库对象
db = SQLAlchemy(app)


@app.route('/')
def index():
    return render_template('layout.html')


# @app.route('/emp/list/')
# def emplist():
#     from pms import Employee
#     items = db.session.query(Employee).limit(10)
#     return render_template('emplist.html', items=items)

from pms import admin
app.register_blueprint(admin, url_prefix='/admin')

from filemanagement import filemaneger
app.register_blueprint(filemaneger, url_prefix='/file')

if __name__ == '__main__':
    app.run()
