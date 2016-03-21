'''
Trying batch action from:
https://flask-admin.readthedocs.org/en/latest/advanced/#customizing-batch-actions

my db notes..
ALTER TABLE user ADD COLUMN active boolean;
ALTER TABLE user ADD COLUMN confirmed_at datetime;

'''
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from wtforms import fields, widgets
import flask_admin as admin
from flask_admin.contrib import sqla
from flask import request, Blueprint, render_template, jsonify, flash, redirect, url_for
from flask_admin.actions import action
import gettext, time, datetime

# Create application
app = Flask(__name__)
app.config['SECRET_KEY'] = '123456790'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fground.sqlite'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)

# Model
class List(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_a = db.Column(db.Unicode(64))
    tag_f1 = db.Column(db.String(255))

    def __unicode__(self):
        return self.name

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())

    def __str__(self):
        return self.email
		
        
class UserView(sqla.ModelView):
    @action('approve', 'Approve', 'Are you sure you want to approve selected users?')
    def action_approve(self, ids):
        try:
            query = User.query.filter(User.id.in_(ids))

            count = 0
            for user in query.all():

                #import pdb;  pdb.set_trace()
                user.active = 1
                user.confirmed_at = datetime.datetime.fromtimestamp(time.time())
                db.session.commit()
                count += 1

            flash('User was successfully approved.'  )
        
        except Exception as ex:
            if not self.handle_view_exception(ex):
                raise

            flash(gettext('Failed to approve users. %(error)s', error=str(ex)), 'error')        
        

# Flask views
@app.route('/')
def index():
    return '<a href="/admin/">Click me to get to Admin!</a>'

if __name__ == '__main__':
    admin = admin.Admin(app, name="batch action" , template_mode='bootstrap3')
    admin.add_view(UserView(User, db.session))
    db.create_all()
    app.run(debug=True)
