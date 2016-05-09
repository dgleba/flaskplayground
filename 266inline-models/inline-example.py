'''
    inline models example..
    http://stackoverflow.com/questions/21968176/flask-flask-admin-one-to-many-cascade
'''
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import flask_admin as admin
from flask_admin.contrib import sqla
from wtforms import SelectField
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import column_property
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Date, DateTime, Enum, ForeignKey, Index, Integer, SmallInteger, String, Table, Text, text, Float, LargeBinary, Numeric
import os
from flask import Flask, url_for, redirect, render_template, request, abort
from flask_security import Security, SQLAlchemyUserDatastore, UserMixin, RoleMixin, login_required, current_user
from flask_security.utils import encrypt_password
import flask_admin
from flask_admin import helpers as admin_helpers
from flask.ext.admin import Admin, BaseView, expose

app = Flask(__name__)  # Create application
app.config['SECRET_KEY'] = '12345679'  # Create dummy secrey key so we can use sessions
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///testflask.sqlite' # Create database
db = SQLAlchemy(app)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class Candidat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(128))
    lastname = db.Column(db.String(128))
    birthdate = db.Column(db.Date)
    '''categories = db.relationship('Category', secondary=category_candidat,
                                 backref=db.backref('candidat', lazy='dynamic'))'''

    def __repr__(self):
        return '<Nom %r>' % self.lastname


class Language(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))

    def __repr__(self):
        return '%s' % unicode(self.name)


class Languagelevel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))

    def __repr__(self):
        return '%s' % self.name

class CandidatLanguage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    candidat_id = db.Column(db.Integer, db.ForeignKey('candidat.id'))
    language_id = db.Column(db.Integer, db.ForeignKey('language.id'))
    language_level_id = db.Column(db.Integer, db.ForeignKey('languagelevel.id'))

    language = db.relationship(Language, backref="Candidat")
    candidat = db.relationship(Candidat, backref="Langue")
    languagelevel = db.relationship(Languagelevel, backref="Candidat")
    
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class MyView(BaseView):
    @expose('/')
    def index(self):
        return self.render('adm-index.html')

admin = Admin(app)
admin.add_view(MyView(name='Hello'))

from flask.ext.admin.contrib.sqla import ModelView

class CandidatView(ModelView):
    column_auto_select_related = True
    inline_models = (CandidatLanguage,)

admin.add_view(CandidatView(Candidat, db.session))
admin.add_view(ModelView(Language, db.session))
admin.add_view(ModelView(Languagelevel, db.session))
    
    
if __name__ == '__main__':

    # Create DB
    db.create_all()

    # Start app
    app.run(debug=True)
    