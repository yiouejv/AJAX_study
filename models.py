# encoding: utf-8
'''
    author: yiouejv
    email: yiouejv@126.com
    blog: blog.syzyb.com
'''

from config import Base
from sqlalchemy import Column, Integer, String


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)
    name = Column(String(50), nullable=False)

Base.metadata.create_all()
