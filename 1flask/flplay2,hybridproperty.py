#
# purpose: 
# -get 3 columns from customer table. 2016-02-08_Mon_13.38-PM works!
# -reflect one table and define another directly with class. works.
# -derived/calculated/grafted column. works.
# -custom template with custom CSS - full width of screen - dgmaster.html. works.
# 
# orginally from flask-admin auth example.
#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


from flask import Flask
from flask import abort
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from flask.ext.admin import Admin
from flask.ext.admin.contrib.sqla import ModelView
import flask_admin as admin
import flask_admin
from flask_admin import helpers as admin_helpers
from flask_admin.contrib import sqla
from flask_admin.contrib.sqla import ModelView
from flask_admin.contrib.sqla.filters import IntGreaterFilter
from flask_security import RoleMixin
from flask_security import SQLAlchemyUserDatastore
from flask_security import Security
from flask_security import UserMixin
from flask_security import current_user
from flask_security import login_required
from flask_security.utils import encrypt_password
from flask_sqlalchemy import SQLAlchemy
import os
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import column_property


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Create Flask application

app = Flask(__name__)
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# reflect some tables

connection = db.engine.connect()
db.metadata.reflect(db.engine, only=['Album'])
Base = automap_base(metadata=db.metadata)
Base.prepare()

dbc_album = Base.classes.Album
    
#    def __str__(self):
#        return self.ArtistId


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Define models directly without reflection...

class Customer(db.Model, UserMixin):
    CustomerId = db.Column(db.Integer(), primary_key=True)
    FirstName = db.Column(db.Unicode(40))
    LastName = db.Column(db.String(20))
    Company = db.Column(db.Unicode(80))
    Address = db.Column(db.Unicode(70))
    City = db.Column(db.Unicode(40))
    State = db.Column(db.Unicode(40))
    Country = db.Column(db.Unicode(40))
    PostalCode = db.Column(db.Unicode(10))
    Phone = db.Column(db.Unicode(24))
    Fax = db.Column(db.Unicode(24))
    Email = db.Column(db.Unicode(60), nullable=False)
    
    @hybrid_property
    def fullname(self):
        return self.FirstName + " " + self.LastName
 
    def __str__(self):
        return self.CustomerId

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
     
# security - user roles tables...
				
		
roles_users = db.Table(
                       'roles_users',
                       db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
                       db.Column('role_id', db.Integer(), db.ForeignKey('role.id'))
                       )

class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

    def __str__(self):
        return self.name

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())
    roles = db.relationship('Role', secondary=roles_users,
                            backref=db.backref('users', lazy='dynamic'))

    def __str__(self):
        return self.email

		
# Setup Flask-Security

user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# Create customized model view class with security and common items.

class MyModelView(sqla.ModelView):
    
    #items common on all list views...
    column_display_pk = True
    can_view_details = True
    can_export = True
    
    def is_accessible(self):
        if not current_user.is_active or not current_user.is_authenticated:
            return False

        if current_user.has_role('superuser'):
            return True

        return False

    def _handle_view(self, name, ** kwargs):
        """
        Override builtin _handle_view in order to redirect users when a view is not accessible.
        """
        if not self.is_accessible():
            if current_user.is_authenticated:
                # permission denied
                abort(403)
            else:
                # login
                return redirect(url_for('security.login', next=request.url))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Flask views

@app.route('/')

def index():
    return render_template('index.html')

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Create admin

admin = flask_admin.Admin(app,  'flaskplayground', 
                          base_template='dgmaster.html', template_mode='bootstrap3',)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# customize tables

class customer_view(MyModelView):

    column_display_pk = True
    can_delete = False
    page_size = 20
    can_view_details = True
    # column_default_sort = ('part_timestamp', True)
    can_export = True
    
    column_list = ['CustomerId', 'Company', 'Email', 'Address', 'City', 'State', 'Country', 'PostalCode', 'Phone', 'fullname']
    
    column_exclude_list = ['Address']
   
    column_searchable_list = ['CustomerId', 'Company', 'Address', 'City', 'State', 'Country', 'PostalCode', 'Phone', 'Fax', 'Email', 'FirstName', 'LastName',]
    
    # make sure the type of your filter matches your hybrid_property
    column_filters = ['FirstName', 'LastName', 'Company', 'Address', 'City', 'State', 'Country', 'PostalCode', 'Phone', 'Fax', \
     'Email'   ]

    #column_filters = [IntGreaterFilter(Screen.number_of_pixels,  'Number of Pixels')]
    
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Add model views

#admin.add_view(customer_view(Customer, db.session))
#admin.add_view(MyModelView(dbc_album, db.session))

#admin.add_view(MyModelView(Role, db.session))
admin.add_view(MyModelView(User, db.session))
   
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# define a context processor for merging flask-admin's template context into the
# flask-security views.
@security.context_processor
def security_context_processor():
    return dict(
                admin_base_template=admin.base_template,
                admin_view=admin.index_view,
                h=admin_helpers,
                )

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# build sample user data

def build_sample_db():
    """
    Do this, or just run the sql to create the users/roles tables...
    
    Populate a small db with some example entries.
    """

    import string
    import random

    #db.drop_all()
    db.create_all()
 
    with app.app_context():
        user_role = Role(name='user')
        super_user_role = Role(name='superuser')
        db.session.add(user_role)
        db.session.add(super_user_role)
        db.session.commit()

        test_user = user_datastore.create_user(
                                               first_name='Admin',
                                               email='admin',
                                               password=encrypt_password('admin'),
                                               roles=[user_role, super_user_role]
                                               )

        db.session.commit()
    return

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

if __name__ == '__main__':

    # Build a sample sqlite db on the fly, if one does not exist yet.
    app_dir = os.path.realpath(os.path.dirname(__file__))
    database_path = os.path.join(app_dir, app.config['DATABASE_FILE'])
    #uncomment to build.... 
    #if not os.path.exists(database_path):
        #build_sample_db()

 
    # Start app
    app.run(host='0.0.0.0', port=5001, debug=True)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

