# encoding: utf-8
'''
    author: yiouejv
    email: yiouejv@126.com
    blog: blog.syzyb.com
'''
from sqlalchemy.orm import relationship, backref

from config import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)
    name = Column(String(50), nullable=False)

    def to_dict(self):
        d = {
            "id": self.id,
            'username': self.username,
            'password': self.password,
            'name': self.name
        }
        return d



class Province(Base):
    __tablename__ = 'province'
    id = Column(Integer, primary_key=True, autoincrement=True)
    province_name = Column(String(50), nullable=False)

    def to_dict(self):
        d = {
            "id": self.id,
            "province_name": self.province_name
        }
        return d


class City(Base):
    __tablename__ = 'city'
    id = Column(Integer, primary_key=True, autoincrement=True)
    city_name = Column(String(50), nullable=False)
    pid = Column(Integer, ForeignKey('province.id'))

    province = relationship('Province', backref=backref('citys'))

    def to_dict(self):
        d = {
            "id": self.id,
            "city_name": self.city_name,
            "pid": self.pid
        }
        return d


Base.metadata.create_all()
