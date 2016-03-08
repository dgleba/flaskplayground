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

class carForm(Form):
    desc     = TextField('desc', [validators.Length(min=4, max=25)])
    
def register(request):
    form = carForm(request.POST)
    if request.method == 'POST' and form.validate():
        car = Car()
        car.desc = form.desc.data
        car.save()
        redirect('register')
    return render_response('form1view3.html', form=form)

# Create admin
admin = admin.Admin(app, name='31form', template_mode='bootstrap3')
admin.add_view(form1View(name='form1', endpoint='form1'))
admin.add_view(CarAdmin(Car, db.session))

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
