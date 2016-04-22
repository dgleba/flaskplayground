''' 
Example: 
Full featured project. 
'''
import os
from flask import Flask, url_for, redirect, render_template, request, abort
from flask_sqlalchemy import SQLAlchemy
from flask_security import Security, SQLAlchemyUserDatastore, \
    UserMixin, RoleMixin, login_required, current_user
from flask_security.utils import encrypt_password
import flask_admin
from flask_admin.contrib import sqla
from flask_admin import helpers as admin_helpers

# import current path. not needed here.
import os, sys
sys.path.insert(0, os.getcwd())

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

app = Flask(__name__)  # Create application
app.config.from_pyfile('config.py')
app.config.from_pyfile('creden.py')
db = SQLAlchemy(app)
    
from  .models import *
from  .views import *
from  .rbac import *
from  .routes import *
    
# Create admin
admin = flask_admin.Admin(
    app, 'Full Feature App', base_template='my_master.html', template_mode='bootstrap3',
)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Add model views
admin.add_view(SuperView(Role, db.session))
admin.add_view(SuperView(Users, db.session))
admin.add_view(customer_view(Customer, db.session))
admin.add_view(lookupRbacView(City, db.session))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# Setup Flask-Security
user_datastore = SQLAlchemyUserDatastore(db, Users, Role)
security = Security(app, user_datastore)

    
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

def build_sample_db():
    """
    Populate a small db with some example entries.
    """
    import string

    #db.drop_all()
    db.create_all()

    with app.app_context():
        read_role = Role(name='read')
        user_role = Role(name='user')
        super_user_role = Role(name='adminrole')
        db.session.add(user_role)
        db.session.add(super_user_role)
        db.session.add(Role(name='create'))     
        db.session.add(Role(name='supervisor'))
        db.session.add(Role(name='delete'))
        db.session.add(Role(name='export'))
        db.session.add(read_role)
        db.session.commit()

        test_user = user_datastore.create_user(
            first_name='Admin',
            email='admin',
            username='admin',
            password=encrypt_password('admin'),
            roles=[user_role, super_user_role]
        )
        
        first_names = [
            'read', 'create', 'user', 'suser',  'delete',    'Mia',
        ]
        last_names = [
            'Brown', 'Smith',  'Patel', 'Jones', 'Williams',  'Thomas',
        ]
 
        for i in range(len(first_names)):
            tmp_username = first_names[i].lower()
            # initialize the users with simple password...  'a'
            tmp_pass = 'a'
            user_datastore.create_user(
                first_name=first_names[i],
                last_name=last_names[i],
                username=tmp_username,
                password=encrypt_password(tmp_pass),
                roles=[read_role ]
            )
        db.session.commit()
    return
