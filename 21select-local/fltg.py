#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''
select widget - local list - for small lists like shift: day night afternoon.
ref.
http://stackoverflow.com/questions/31081516/how-can-i-turn-a-string-model-field-into-a-select-input-in-flask-admin

'''
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import flask_admin as admin
from flask_admin.contrib import sqla
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import column_property, relationship
from flask_admin.contrib.sqla import ModelView
from sqlalchemy import Column, Integer, String, ForeignKey, String, Table, Text
from sqlalchemy.ext.declarative import declarative_base
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from flask_admin.form.widgets import Select2Widget
from wtforms import SelectField

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
db.metadata.reflect(bind=db.engine, only=['users','Persons'])
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#reflect table...   
class users(db.Model):
    __table__ = db.Table('users', db.metadata,
        autoload=True, autoload_with=db.engine
    )
   
class persons(db.Model):
    __table__ = db.Table('Persons', db.metadata,
        autoload=True, autoload_with=db.engine
    )
    
'''
class cities(db.Model):
    __table__ = db.Table('cities', db.metadata,
        autoload=True, autoload_with=db.engine
    )
'''
 
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Flask views
@app.route('/')
def index():
    return '<a href="/admin/">Click me to get to Admin!</a>'
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# customize views..
  
class dvview(sqla.ModelView):
    column_display_pk = True

class persons_view(dvview):
    form_overrides = dict(
        city=SelectField
    )
    form_args = dict(
        city=dict(
            choices=[
                ('London1', 'London'),
                ('Kitchener1', 'Kitchener')
            ]
        )
    )
    def __init__(self):
        super(persons_view, self).__init__(persons, db.session)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Create admin
admin = admin.Admin(app, name='fltg 21selectlocal', template_mode='bootstrap3')

admin.add_view(dvview(users, db.session))
admin.add_view(persons_view(persons, db.session))
#admin.add_view(dvview(cities, db.session))
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
if __name__ == '__main__':
    # Start app
    app.run(host='0.0.0.0', port=5000, debug=True)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
