'''
add some roles like readonly and create
'''
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from flask import Flask, abort, redirect, render_template, request
from flask import url_for
from flask.ext.admin import Admin
from flask.ext.admin.contrib.sqla import ModelView
import flask_admin as admin
import flask_admin
from flask_admin import helpers as admin_helpers
from flask_admin.contrib import sqla
from flask_admin.contrib.sqla import ModelView
from flask_admin.contrib.sqla.filters import IntGreaterFilter
from flask_security import RoleMixin, SQLAlchemyUserDatastore, Security
from flask_security import UserMixin, current_user, login_required
from flask_security.utils import encrypt_password
from flask_sqlalchemy import SQLAlchemy
import os
from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import column_property

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Create Flask application
app = Flask(__name__)
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
connection = db.engine.connect()
Base = automap_base(metadata=db.metadata)
Base.prepare()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Define models directly without reflection...

class Customer(db.Model):
    CustomerId = db.Column(db.Integer(), primary_key=True)
    FirstName = db.Column(db.Unicode(40), nullable=False)
    LastName = db.Column(db.String(20), nullable=False)
    City = db.Column(db.Unicode(40))
    Email = db.Column(db.Unicode(60))
 
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

class rbacBaseView(ModelView):
            
    def is_accessible(self):
        if not current_user.is_active or not current_user.is_authenticated:
            return False
        if current_user.has_role('superuser'):
            return True
        return False

    def _handle_view(self, name, ** kwargs):
        
        if current_user.has_role('read'):
            print "i am read"
            can_create = False
            can_edit = False
            can_delete = False
            can_export = False

        if current_user.has_role('superuser'): 
            print 'i am superuser'
            can_edit = False
            can_create = True
            can_delete = True
            can_export = True
        
        #Override builtin _handle_view in order to redirect users when a view is not accessible.
        if not self.is_accessible():
            if current_user.is_authenticated:
                # permission denied
                abort(403)
            else:
                # login
                return redirect(url_for('security.login', next=request.url))
                
    #items common on all list views...
    column_display_pk = True
    page_size = 20
    can_view_details = True
            
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Flask views
@app.route('/')
def index():
    return render_template('index.html')

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Create admin
admin = flask_admin.Admin(app,  'roles', 
                          base_template='dgmaster.html', template_mode='bootstrap3',)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# customize tables

class customer_view(rbacBaseView):

    column_searchable_list = ['CustomerId', 'City',  'Email', 'FirstName', 'LastName',]
    # make sure the type of your filter matches your hybrid_property
    column_filters = ['FirstName', 'LastName',  'City',  'Email'   ]
    # column_default_sort = ('part_timestamp', True)
    
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Add model views
admin.add_view(customer_view(Customer, db.session))
admin.add_view(rbacBaseView(Role, db.session))
admin.add_view(rbacBaseView(User, db.session))
   
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
if __name__ == '__main__':
    app_dir = os.path.realpath(os.path.dirname(__file__))
    database_path = os.path.join(app_dir, app.config['DATABASE_FILE'])
    app.run(host='0.0.0.0', port=5001, debug=True)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
