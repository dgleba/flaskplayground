# Small-Example: cartype is a select field widget. Create or edit a car record to see it working. David Gleba.
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import flask_admin as admin
from flask_admin.contrib import sqla
from wtforms import SelectField

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
    cartype = db.Column(db.String(50))
    desc2 = db.Column(db.String(50))
    desc3 = db.Column(db.String(50))
    desc4 = db.Column(db.String(50))
    desc5 = db.Column(db.String(50))
    desc6 = db.Column(db.String(50))
    desc7 = db.Column(db.String(50))
    desc8 = db.Column(db.String(50))
    desc9 = db.Column(db.String(50))
    desc10 = db.Column(db.String(50))
    desc11 = db.Column(db.String(50))
    desc12 = db.Column(db.String(50))
    desc13 = db.Column(db.String(50))
    desc14 = db.Column(db.String(50))
    desc15 = db.Column(db.String(50))
    desc16 = db.Column(db.String(50))
    desc17 = db.Column(db.String(50))
    desc18 = db.Column(db.String(50))

class CarAdmin(sqla.ModelView):
    form_overrides = dict(cartype=SelectField)
    form_args = dict(cartype=dict(choices=[
                ('', 'Please Select'),
                ('Compact', 'Compact'),
                ('Mid-size', 'Mid-size'),
                ('Pickup Truck', 'Pickup Truck')
            ]))
    column_descriptions = dict(
        desc='Description of car'   )
        
    # kludge to make a column wider...
    column_labels = dict(desc2='Description2_of_Car__________________',desc5='Description5_of_Car_____',)
    
    
# Create admin
admin = admin.Admin(app, name='Column width Kludge', template_mode='bootstrap3')
admin.add_view(CarAdmin(Car, db.session))

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
