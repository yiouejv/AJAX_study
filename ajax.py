# encoding: utf-8
'''
    author: yiouejv
    email: yiouejv@126.com
    blog: blog.syzyb.com
'''

from flask import Blueprint, request, render_template
from flask import views
from config import session as db_session
from models import User

ajax_bp = Blueprint('ajax', __name__)

@ajax_bp.route('/')
@ajax_bp.route('/index/')
def index():
    return 'index'


@ajax_bp.route('/xmlhttprequest/')
def xmlhttprequest():
    return render_template('ajax/XMLHttpRequest.html')


@ajax_bp.route('/ajax_get/')
def ajax_get():
    return render_template('ajax/ajax_get.html')


@ajax_bp.route('/ajax_server/')
def ajax_server():
    return '这是我的第一个ajax请求'


@ajax_bp.route('/ajax_exercise/')
def ajax_exercise():
    return render_template('ajax/ajax_exercise.html')


@ajax_bp.route('/aes/')
def aes():
    name = request.args.get('name')
    if name:
        return '欢迎'+name
    else:
        return '发送失败'


@ajax_bp.route('/gph/')
def gph():
    return render_template('ajax/post.html')

@ajax_bp.route('/post/', methods=['POST'])
def post():
    form = request.form
    print(form)
    return '姓名：%s, 年龄：%s' % (form.get('name'), form.get('age'))


class RegisterView(views.MethodView):
    def get(self):
        return render_template('ajax/register.html')

    def post(self):
        form = request.form
        username = form.get('username')
        password = form.get('password')
        name = form.get('name')
        if username and password and name:
            user = User(username=username, password=password, name=name)
            db_session.add(user)
            db_session.commit()
            return 'success'
        # 查询数据库中是否存在相同的登录名
        usernames = db_session.query(User).filter(User.username == username).all()
        if not username:
            return '用户名不能为空'
        else:
            if usernames:
                return '登录名已存在'
            else:
                return '用户名合法'



ajax_bp.add_url_rule('/register/', view_func=RegisterView.as_view('register'))