# print column names for a table..
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin.contrib import sqla
from sqlalchemy.orm import column_property, relationship
from sqlalchemy import Column, Integer, String, ForeignKey, String, Table, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import inspect
import sys

app = Flask(__name__)  # Create application
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.sqlite' # Create database
db = SQLAlchemy(app)

#connect and  reflect...
connection = db.engine.connect()  # no need to reflect view...
db.metadata.reflect(bind=db.engine, only=['cars',])
Base = declarative_base()
metadata = Base.metadata

class Cars(db.Model):
    __table__ = db.Table('Cars', db.metadata, autoload=True, autoload_with=db.engine )
     
mapper = inspect(Cars)
# with new lines..
for column in mapper.attrs:
    print "'" + column.key + "',"
print
        
for column in mapper.attrs:
    sys.stdout.write("'" + column.key + "', ")
print
    
#inspect(Cars).columns.keys()
# ??
#Cars.__table__.columns

if __name__ == '__main__':
    app.run()
    #app.run(debug=True)
