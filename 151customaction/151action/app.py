""" new_action.py
    Demonstrates how to add a custom action at the left of a row

    In this case, the action is under the STAR icon in each row

    All credit goes to xmm
     See https://github.com/flask-admin/flask-admin/issues/998
"""

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Enum
from flask_admin.contrib import sqla
from flask_admin import Admin, expose, BaseView
import re

# Create application
app = Flask(__name__)
app.config['SECRET_KEY'] = '123456790'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///a_sample_database.sqlite'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)

# Flask views
@app.route('/')
def index():
    return '<a href="/admin/">Click me to get to Admin!</a>'

class Dog(db.Model):
    __tablename__ = 'pet'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(String(20), nullable=False, unique=True)
    favorite_food = db.Column(Enum('Bones', 'Shoes', 'Newspaper', 'Roadkill'),
                         nullable=True)

class DogAdmin(sqla.ModelView):
    column_editable_list = ('name', 'favorite_food')
    list_template = 'star_list.html'

class MyAdmin(Admin):
    def add_extra_view(self, view):
        """Like Admin.add_view() method, but does not add an item to menu"""
        self._views.append(view)
        if self.app is not None:
            self.app.register_blueprint(view.create_blueprint(self))

# Create admin
admin = MyAdmin(app, name='STAR = custom action', template_mode='bootstrap3')
admin.add_view(DogAdmin(Dog, db.session))

class StarView(BaseView):
    """ The view called by the Star icon in each row """
    @expose('/', methods=('POST',))
    def index(self):
        tbl_name = request.form['tbl_name']
        rowid = request.form['rowid']
        pet_name = request.form['pet_name']
        favorite_food = request.form['favorite_food']
        adminview_dict = request.form['adminview_dict']
        adminview_model_dict = request.form['adminview_model_dict']
        row_dict = request.form['row_dict']

        result = db.engine.execute('''SELECT name FROM pet
                                      WHERE favorite_food = :favorite_food''',
                                   favorite_food=favorite_food)
        similar_pets = [row[0] for row in result]

        # The next three lines are only to show available variables
        # in star_action.html for demo purposes
        DICT_REGEX = re.compile(r"'[^']+':(?:(?!'[^']+':).)+(?=[,}])")
        adminview_data = DICT_REGEX.findall(adminview_dict)
        adminview_model_data = DICT_REGEX.findall(adminview_model_dict)
        row_data = DICT_REGEX.findall(row_dict)

        return self.render('star_action.html', tbl_name=tbl_name, rowid=rowid,
                           pet_name=pet_name, favorite_food=favorite_food,
                           similar_pets=similar_pets,
                           adminview_data=adminview_data, adminview_model_data=adminview_model_data,
                           row_data=row_data)
admin.add_extra_view(StarView())

# Create DB
#db.drop_all()
db.create_all()
'''
db.session.add(Dog(name='Kiki', favorite_food='Shoes'))
db.session.add(Dog(name='Lassie', favorite_food='Shoes'))
db.session.add(Dog(name='Plato', favorite_food='Shoes'))
db.session.add(Dog(name='Scoobydoo', favorite_food='Bones'))
db.session.add(Dog(name='Belle', favorite_food='Bones'))
db.session.add(Dog(name='Einstein', favorite_food='Bones'))
db.session.commit()
'''

# Start app
app.run(debug=True)
