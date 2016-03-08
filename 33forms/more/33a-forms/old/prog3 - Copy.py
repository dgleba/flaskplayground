'''
Small-Example: custom input form

i plan to use flask-wtf and wtf-alchemy to make a form. 2016-03-06

David Gleba.
'''
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import flask_admin as admin
from flask_admin.contrib import sqla
from wtforms import SelectField

app = Flask(__name__)  # Create application
app.config['SECRET_KEY'] = '123456790'  # Create dummy secrey key so we can use sessions
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fground.sqlite' # Create database
db = SQLAlchemy(app)

@app.route('/')  # Flask views
def index():
    return '<a href="/admin/">Click me to get to Admin!</a>'

from flask_admin import BaseView, expose
class form1View(BaseView):
    @expose('/')
    def index(self):
        return self.render('form1view3.html')
 
class students(db.Model):
   id = db.Column('student_id', db.Integer, primary_key = True)
   name = db.Column(db.String(100))
   city = db.Column(db.String(50))  
   addr = db.Column(db.String(200))
   pin = db.Column(db.String(10))

def __init__(self, name, city, addr,pin):
   self.name = name
   self.city = city
   self.addr = addr
   self.pin = pin

   
class Car(db.Model):
    __tablename__ = 'cars'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    desc = db.Column(db.String(50))
    cartype = db.Column(db.String(50))

class CarAdmin(sqla.ModelView):
    form_overrides = dict(cartype=SelectField)
    form_args = dict(cartype=dict(choices=[
                ('', 'Please Select'),
                ('Compact', 'Compact'),
                ('Mid-size', 'Mid-size'),
                ('Pickup Truck', 'Pickup Truck')
            ]))

from wtforms import Form, BooleanField, TextField, validators

@app.route('/new', methods = ['GET', 'POST'])
def new():
   if request.method == 'POST':
      if not request.form['name'] or not request.form['city'] or not request.form['addr']:
         flash('Please enter all the fields', 'error')
      else:
         student = students(request.form['name'], request.form['city'],
            request.form['addr'], request.form['pin'])
         
         db.session.add(student)
         db.session.commit()
         
         flash('Record was successfully added')
         return redirect(url_for('show_all'))
   return render_template('new.html')
   

# Create admin
admin = admin.Admin(app, name='31form', template_mode='bootstrap3')
admin.add_view(CarAdmin(Car, db.session))

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
