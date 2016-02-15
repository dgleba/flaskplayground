#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''
datetime picker

ref. user table in sqla example.

'''

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import flask_admin as admin
from flask_admin.contrib import sqla
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import column_property
from flask_admin.contrib.sqla import ModelView
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy import Column, ForeignKey, Integer, String, Table, Text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

# Create application
app = Flask(__name__)

# Create dummy secrey key so we can use sessions
app.config['SECRET_KEY'] = '12344567901'

# define db engine..
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.sqlite'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#connect and  reflect...

connection = db.engine.connect()
# no need to reflect view...
db.metadata.reflect(bind=db.engine, only=['users'])
 
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#reflect table...   
class users(db.Model):
    __table__ = db.Table(
        'users', db.metadata,
        autoload=True,
        autoload_with=db.engine
    )
   
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
# Flask views
@app.route('/')
def index():
    return '<a href="/admin/">Click me to get to Admin!</a>'

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
   
# customize views..
   
class dgview(sqla.ModelView):
    column_display_pk = True

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 
# Create admin
admin = admin.Admin(app, name='fltg 9datetime picker', template_mode='bootstrap3')

admin.add_view(dgview(users, db.session))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

if __name__ == '__main__':

    # Start app
    app.run(host='0.0.0.0', port=5000, debug=True)
    
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
