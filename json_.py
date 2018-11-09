# encoding: utf-8
'''
    author: yiouejv
    email: yiouejv@126.com
    blog: blog.syzyb.com
'''

from flask import Blueprint, request, render_template
from flask import views
from config import session as db_session
from models import User, Province, City
from flask import jsonify, make_response
import json

json_bp = Blueprint('json', __name__)


@json_bp.route('/all_users/')
def all_users():
    return render_template('json/all_users.html')


@json_bp.route('/all_users_server/')
def all_users_server():
    users = db_session.query(User).all()
    str = ''
    for user in users:
        str = user.username + ',' + user.password + ',' + user.name + '|'
    return str


@json_bp.route('/json/')
def json_():
    return render_template('json/json.html')


@json_bp.route('/json2/')
def json2():
    lst = [
        '范冰冰',
        'Fan Bing Bing',
        'Li Chen'
    ]
    dict = {
        'name': "范冰冰",
        'age': 37,
        'gender': '女'
    }
    ul = [
        {
            'name': 'MrWang',
            'age': 37,
            'gender': 'male'
        },
        {
            'name': 'Mrs Wang',
            'age': 15,
            'gender': 'female'
        }
    ]
    json_str = json.dumps(ul)
    return json_str


@json_bp.route('/json3/')
def json3():
    return render_template('json/json3.html')


@json_bp.route('/json3_server/')
def json3_server():
    ul = [
        {
            'name': 'MrWang',
            'age': 37,
            'gender': 'male'
        },
        {
            'name': 'Mrs Wang',
            'age': 15,
            'gender': 'female'
        }
    ]
    return json.dumps(ul)


@json_bp.route('/json4/')
def json4():
    return render_template('json/json4.html')


@json_bp.route('/json4_server/')
def json4_server():
    users = db_session.query(User).all()
    users = [user.to_dict() for user in users]
    return json.dumps(users)


class ListView(views.MethodView):
    def get(self):
        return render_template('json/list.html')

    def post(self):
        return 'success'


json_bp.add_url_rule('/list/', view_func=ListView.as_view('list'))


@json_bp.route('/get_list/')
def get_list():
    users = db_session.query(User).all()
    users = [user.to_dict() for user in users]
    return json.dumps(users)


@json_bp.route('/provinces/')
def provinces():
    return render_template('json/province_city.html')


@json_bp.route('/get_provinces/')
def get_provinces():
    provinces = db_session.query(Province).all()
    provinces = [province.to_dict() for province in provinces]
    return json.dumps(provinces)


@json_bp.route('/citys/<pid>/')
def citys(pid):
    citys = db_session.query(City).filter(City.pid==pid).all()
    citys = [city.to_dict() for city in citys]
    return json.dumps(citys)


@json_bp.route('/load/')
def load():
    return render_template('json/load.html')


@json_bp.route('/load_server/', methods=['GET', 'POST'])
def load_server():
    if request.method == 'POST':
        name = request.form['name']
        return 'name: %s' % name
    else:
        return '响应回去的数据'


@json_bp.route('/jq_ajax/')
def jq_ajax():
    return render_template("json/jq_ajax.html")


