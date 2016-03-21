''' 
Small-Example: 
modular .py files project. 
originally based on ...\VCS-git\flaskplay\25selectlocal-eg
cartype is a select field widget. Create or edit a car record to see it working. David Gleba.
'''
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import flask_admin as admin
from flask_admin.contrib import sqla
from wtforms import SelectField
# import current path. not needed here.
import os, sys
sys.path.insert(0, os.getcwd())

app = Flask(__name__)  # Create application
app.config['SECRET_KEY'] = '123456790'  # Create dummy secrey key so we can use sessions
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.sqlite' # Create database
db = SQLAlchemy(app)

from  .models import *
from  .views import *
    
# Create admin    
db.create_all()  
admin = admin.Admin(app, name='Select - from Local list', template_mode='bootstrap3')
admin.add_view(CarAdmin(Car, db.session))

