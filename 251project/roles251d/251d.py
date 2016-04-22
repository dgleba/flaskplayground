# coding: utf-8
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class FsRole(Base):
    __tablename__ = 'fs_role'

    id = Column(Integer, primary_key=True)
    name = Column(String(80))
    description = Column(String(255))

    fs_users = relationship(u'FsUser', secondary='fs_user_role')
    users = relationship(u'FsUser', secondary='roles_users')


class FsUser(Base):
    __tablename__ = 'fs_user'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(255))
    last_name = Column(String(255))
    email = Column(String(255), unique=True)
    password = Column(String(255))
    active = Column(Integer)
    confirmed_at = Column(DateTime)
    username = Column(String(45), nullable=False, unique=True)


t_fs_user_role = Table(
    'fs_user_role', metadata,
    Column('fs_user_id', ForeignKey(u'fs_user.id'), nullable=False, index=True),
    Column('fs_role_id', ForeignKey(u'fs_role.id'), nullable=False, index=True)
)


t_roles_users = Table(
    'roles_users', metadata,
    Column('user_id', ForeignKey(u'fs_user.id'), index=True),
    Column('role_id', ForeignKey(u'fs_role.id'), index=True)
)
