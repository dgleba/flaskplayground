''' small-Example: cartype was a select field widget. Create or edit a car record to try it. David Gleba.
http://stackoverflow.com/questions/14591202/how-to-make-a-radiofield-in-flask
'''
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import flask_admin as admin
from flask_admin.contrib import sqla
from wtforms import RadioField
from flask_admin.contrib.sqla import ModelView
from flask_admin.form import rules

app = Flask(__name__)  # Create application
app.config['SECRET_KEY'] = '123456790'  # Create dummy secrey key so we can use sessions
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.sqlite' # Create database
db = SQLAlchemy(app)

@app.route('/')  # Flask views
def index():
    return '<a href="/admin/">Click me to get to Admin!</a>'

class Car(db.Model):
    __tablename__ = 'cars'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    desc = db.Column(db.String(50))
    cartype = db.Column(db.Text)
    comment = db.Column(db.Text)

class CarAdmin(ModelView):
    # Didn't need this ...
    #form_create_rules = ('desc', 'cartype', rules.HTML('<br><br>'), 'comment' )  # add some space after cartype...
        # I didn't get this to work:   rules.Container ( 'CarTypeMacro1', rules.Field('cartype') )
        
    # use a radiofield...
    form_overrides = dict(cartype=RadioField)
    form_args = dict(cartype=dict(choices=[
                ('Compact', 'Compact'),
                ('Mid-size', 'Mid-size'),
                ('Pickup-Truck', 'Pickup Truck')
            ]))
    # Use CSS to change look of the field.  http://stackoverflow.com/questions/31547401/adjust-field-size-in-flask-admin-w-bootstrap3
    form_widget_args = {
    'cartype':{'class': 'form-control, width: 0.01%',
               #'style': "width: 1%",
               #'placeholder':'ex. M132 or T456'
               }
    }           
     
# Create admin
admin = admin.Admin(app, name='Radiofield', template_mode='bootstrap3')
admin.add_view(CarAdmin(Car, db.session))

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
