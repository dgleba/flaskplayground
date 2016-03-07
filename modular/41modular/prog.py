''' 
Small-Example: 
modular .py files. 
based on C:\n\Dropbox\csd\VCS-git\flaskplay\25selectlocal-eg
cartype is a select field widget. Create or edit a car record to see it working. David Gleba.
'''
from flask import Flask
import flask_admin as admin
from flask_admin.contrib import sqla
from wtforms import SelectField
# import current path. not needed here.
import os, sys
sys.path.insert(0, os.getcwd())

from models import models

app = Flask(__name__)  # Create application
app.config['SECRET_KEY'] = '123456790'  # Create dummy secrey key so we can use sessions
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.sqlite' # Create database


@app.route('/')  # Flask views
def index():
    return '<a href="/admin/">Click me to get to Admin!</a>'

class CarAdmin(sqla.ModelView):
    form_overrides = dict(cartype=SelectField)
    form_args = dict(cartype=dict(choices=[
                ('', 'Please Select'),
                ('Compact', 'Compact'),
                ('Mid-size', 'Mid-size'),
                ('Pickup Truck', 'Pickup Truck')
            ]))
    
# Create admin
admin = admin.Admin(app, name='Select - from Local list', template_mode='bootstrap3')
admin.add_view(CarAdmin(Car, db.session))

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
