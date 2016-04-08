''' 
make a password to copy paste into other db...
'''
import os
from flask import Flask, url_for, redirect, render_template, request, abort
from flask_sqlalchemy import SQLAlchemy
from flask_security import Security, SQLAlchemyUserDatastore, UserMixin, RoleMixin, login_required, current_user
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
    app, 'gen password', base_template='my_master.html', template_mode='bootstrap3',
)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Add model views
admin.add_view(SuperView(Role, db.session))
admin.add_view(SuperView(User, db.session))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# Setup Flask-Security
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
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
    Populate user pass...
    """
    import string

    with app.app_context():
        
        user_role = Role(name='user')
        super_user_role = Role(name='adminrole')

        #set user / pass in creden.py
        uname=app.config['USER1']
        
        test_user = user_datastore.create_user(
            first_name=uname,
            email=uname,
            password=encrypt_password(app.config['PASS1']),
            roles=[user_role, super_user_role]
        )
        
        db.session.commit()
    return
