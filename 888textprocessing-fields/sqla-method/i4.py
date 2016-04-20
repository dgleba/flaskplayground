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

d = {k: metadata.tables[k].columns.keys() for k in metadata.tables.keys()}

print(d)


#connect and  reflect...

class Cars(engine.Model):
    __table__ = engine.Table('Cars', engine.metadata, autoload=True, autoload_with=engine.engine )
     
mapper = inspect(Cars)
# with new lines..
for column in mapper.attrs:
    print "'" + column.key + "',"
print
        
for column in mapper.attrs:
    sys.stdout.write("'" + column.key + "', ")
print


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

'''
mysql only...
from sqlalchemy.sql import text
cmd = "SELECT * FROM information_schema.columns WHERE table_schema = :db ORDER BY table_name,ordinal_position"
result = session.execute(
            text(cmd),
            {"db": "classicmodels"}
        )
result.fetchall()
'''
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# for m in session.query(cilisting1.__table__.columns).all():
    # print m
    
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
# from sqlalchemy.inspection import inspect
# table = inspect(model)
# for column in table.c
    # print column.name

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# from sqlalchemy import inspect
# inst = inspect(cilisting1)
# attr_names = [c_attr.key for c_attr in inst.mapper.column_attrs]


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''
model = session.cars
columns = [m.key for m in model.__table__.columns]
'''
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# for m in session.query(model).all():
    # print [getattr(m, x.__str__().split('.')[1]) for x in model.__table__.columns]
    # # additional code 
    
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
