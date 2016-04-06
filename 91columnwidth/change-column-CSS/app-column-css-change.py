'''
CSS change for one column header
'''
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from wtforms import fields, widgets
import flask_admin as admin
from flask_admin.contrib import sqla
from flask import request, Blueprint, render_template, jsonify, flash, redirect, url_for

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
    def __str__(self):
        return self.email

# Flask views
@app.route('/')
def index():
    return '<a href="/admin/">Click me to get to Admin!</a>'

# query for multiple autocomplete field
@app.route('/ue_autocomplete', methods=['GET'])
def tag_f1_autocomplete():
    search = request.args.get('q')
    query = db.session.query(User.email).filter(User.email.like('%' + str(search) + '%'))
    results = [mv[0] for mv in query.all()]
    return jsonify(matching_results=results)
     
# Customized admin interface
class ListAdminView(sqla.ModelView):
    list_template = 'list.html'
    create_template = 'edit.html'
    edit_template = 'edit.html'
    can_export=True

if __name__ == '__main__':
    # Create admin
    admin = admin.Admin(app, name="Column header CSS" , template_mode='bootstrap3')
    admin.add_view(ListAdminView(List, db.session))
    db.create_all()
    app.run(debug=True)
