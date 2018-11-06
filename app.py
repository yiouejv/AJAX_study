from flask import Flask, render_template, request
from flask import views
from config import session as db_session
from models import User

app = Flask(__name__)


@app.route('/')
@app.route('/index/')
def index():
    return 'index'


@app.route('/xmlhttprequest/')
def xmlhttprequest():
    return render_template('XMLHttpRequest.html')


@app.route('/ajax_get/')
def ajax_get():
    return render_template('ajax_get.html')


@app.route('/ajax_server/')
def ajax_server():
    return '这是我的第一个ajax请求'


@app.route('/ajax_exercise/')
def ajax_exercise():
    return render_template('ajax_exercise.html')


@app.route('/aes/')
def aes():
    name = request.args.get('name')
    if name:
        return '欢迎'+name
    else:
        return '发送失败'


@app.route('/gph/')
def gph():
    return render_template('post.html')

@app.route('/post/', methods=['POST'])
def post():
    form = request.form
    print(form)
    return '姓名：%s, 年龄：%s' % (form.get('name'), form.get('age'))


class RegisterView(views.MethodView):
    def get(self):
        return render_template('register.html')

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



app.add_url_rule('/register/', view_func=RegisterView.as_view('register'))



if __name__ == '__main__':
    app.run()
