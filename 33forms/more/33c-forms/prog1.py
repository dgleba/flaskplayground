'''
 result: see err.txt
 
 ref.  http://thomasbhatia.blogspot.ca/2012/10/flask-mysql-wtforms-sqlalchemy-that.html
 and wtforms crash course
 
'''

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import flask_admin as admin
from flask_admin.contrib import sqla
from wtforms import Form, BooleanField, StringField, validators
from wtforms import Form, StringField, validators, PasswordField, SelectField

from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
#!/usr/bin/env python
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy.interfaces

app = Flask(__name__)
# Create dummy secrey key so we can use sessions
app.config['SECRET_KEY'] = '1234567901'

# Without this, MySQL will silently insert invalid values in the
# database, causing very long debugging sessions in the long run
# source: http://www.enricozini.org/2012/tips/sa-sqlmode-traditional/
class DontBeSilly(sqlalchemy.interfaces.PoolListener):
    def connect(self, dbapi_con, connection_record):
        cur = dbapi_con.cursor()
        cur.execute("SET SESSION sql_mode='TRADITIONAL'")
        cur = None

#engine = create_engine('mysql+mysqldb://root:banana@127.0.0.1/testdb?charset=utf8&use_unicode=0', convert_unicode=True, listeners=[DontBeSilly()], echo=True)
engine = create_engine('sqlite:///fground.sqlite', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,autoflush=False,bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()
Base.metadata.create_all(bind=engine)


#!/usr/bin/env python
from sqlalchemy import Column, Integer, String
#from flask_application.database import Base
  
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
    email = Column(String, unique=True)
    country_id = Column(Integer)

    def __init__(self, username, password, email, country_id):
        self.username = username
        self.password = password
        self.email = email
        self.country_id = country_id

    def __repr__(self):
        return '<user %r="">' % (self.username, self.password, self.email, self.country_id) %  '</user>'

#!/usr/bin/env python
#from flask.ext.wtf import Form, TextField, PasswordField, BooleanField, SelectField
#from flask.ext.wtf import Required, Email, EqualTo
    
class user_add_form(Form):
    username = StringField('Username')
    password = PasswordField('Password')
    confirm = PasswordField('Repeat Password')
    email = StringField('Email')
    country_id = SelectField(u'Country', choices=[('1', 'UK - United Kingdom')])
   
'''class RegistrationForm(Form):
    username     = StringField('Username', [validators.Length(min=4, max=25)])
    email        = StringField('Email Address', [validators.Length(min=6, max=35)])
    accept_rules = BooleanField('I accept the site rules', [validators.InputRequired()])   
'''
   
from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for
#from flask import app
#from flask.database import db_session
#from flask.models import User
#from flask.forms import user_add_form
#from werkzeug.security import generate_password_hash, check_password_hash   

# Flask views
@app.route('/')
def index():
    return '<a href="/admin/">Click me to get to Admin!</a>'

    
@app.route('/new', methods = ['GET', 'POST'])

def register(request):
    form = User_Add_Form(request.POST)
    if request.method == 'POST' and form.validate():
        user = User()
        user.username = form.username.data
        user.email = form.email.data
        user.save()
        redirect('register')
    return render_response('register.html', form=form)
 
'''
def users_add():
    if form.validate_on_submit():
        new_user = User(
                    form.username.data,
                    generate_password_hash(form.password.data),
                    form.email.data,
                    form.country_id.data
                    )
        db_session.add(new_user)
        db_session.commit()
        
    return render_template('template_add_user.html', form=form)    
''' 
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
  
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    