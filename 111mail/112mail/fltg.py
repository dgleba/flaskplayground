#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''
mail button on details view will send current record
'''
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from flask import Flask, render_template, request, flash
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
#secrets...
import creds
app.config.from_pyfile('creds.py')

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#connect and  reflect...
connection = db.engine.connect()
# no need to reflect view...
db.metadata.reflect(bind=db.engine, only=['users','Persons'])
Base = declarative_base()
metadata = Base.metadata

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

from flask.ext.mail import Message, Mail
mail = Mail()
app.config["MAIL_SERVER"] = "smtp.live.com"
app.config["MAIL_PORT"] = 587
app.config["MAIL_USE_TLS"] = True
#app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = creds.cred['mailu']
app.config["MAIL_PASSWORD"] = creds.cred['mailpass']
mail.init_app(app)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#reflect table...   
class users(db.Model):
    __table__ = db.Table('users', db.metadata,
        autoload=True, autoload_with=db.engine
    )
   
class Person(db.Model):
    __table__ = db.Table('Persons', db.metadata,
        autoload=True, autoload_with=db.engine
    )
    
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Flask views
@app.route('/')
def index():
    return '<a href="/admin/">Click me to get to Admin!</a>'
    
@app.route('/sendmail1')
def msendmail1():
    "{{ get_url('.details_view', id=get_pk_value(row), url=return_url) }}" title="{{ _gettext('View Record') }}"
    msg = Message('test-sendmail1-9-f-20160314', sender=creds.cred['mailu'], recipients=['dgleba@gmail.com'])
    msg.body = """
    From: %s <%s>
    %s
    """ % ('dave', creds.cred['mailu'], 'testdata392')
    mail.send(msg)
    return ('<br><br><hr> Mail send processed. Press your browser BACK button.<hr>')
    
    
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# customize views..
  
class drView(ModelView):
    column_display_pk = True
    can_view_details = True

class persons_view(drView):
    details_template = 'details.html'
    form_overrides = dict(City=SelectField)
    form_args = dict(City=dict(choices=[
                ('', 'Please Select'),
                ('London', 'London'),
                ('Kitchener', 'Kitchener')
            ]
        )
    )
    
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Create admin
admin = admin.Admin(app, name='fltg 21selectlocal', template_mode='bootstrap3')

admin.add_view(drView(users, db.session))
admin.add_view(persons_view(Person, db.session))
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
if __name__ == '__main__':
    # Start app
    app.run(host='0.0.0.0', port=5000, debug=True)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
