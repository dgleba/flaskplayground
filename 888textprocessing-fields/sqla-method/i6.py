"""
read table, print columns.
http://stackoverflow.com/questions/6039342/how-to-print-all-columns-in-sqlalchemy-orm

"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
# print column names for a table..
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin.contrib import sqla
from sqlalchemy.orm import column_property, relationship
from sqlalchemy import Column, Integer, String, ForeignKey, String, Table, Text
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import inspect
import sys

engine = create_engine('sqlite:///test.sqlite')
DeclarativeBase = declarative_base()
metadata = DeclarativeBase.metadata
metadata.bind = engine

# configure Session class with desired options
Session = sessionmaker()
# associate it with our custom Session class
Session.configure(bind=engine)
# work with the session
session = Session()


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 
for m in session.query(*model.__table__.columns).all():
    print m



    
