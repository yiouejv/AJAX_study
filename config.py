# encoding: utf-8
'''
    author: yiouejv
    email: yiouejv@126.com
    blog: blog.syzyb.com
'''

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import sessionmaker

HOST = '127.0.0.1'
PORT = 3306
DATABASE = 'ajax'
USERNAME = 'root'
PASSWORD = 123456

DB_URL = "mysql+pymysql://{username}:{password}@{host}:{port}/{db}".format(
    username=USERNAME, password=PASSWORD, host=HOST, port=PORT, db=DATABASE
)
engine = create_engine(DB_URL)
Base = declarative_base(engine)
session = sessionmaker(engine)()