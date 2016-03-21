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

''' Define a wtforms widget and field.
    WTForms documentation on custom widgets:
    http://wtforms.readthedocs.org/en/latest/widgets.html#custom-widgets
'''
class CKTextAreaWidget(widgets.TextArea):
    def __call__(self, field, **kwargs):
        # add WYSIWYG class to existing classes
        existing_classes = kwargs.pop('class', '') or kwargs.pop('class_', '')
        kwargs['class'] = u'%s %s' % (existing_classes, "ue_autocomplete")
        return super(CKTextAreaWidget, self).__call__(field, **kwargs)

class CKTextAreaField(fields.TextAreaField):
    widget = CKTextAreaWidget()

# Model
class Page(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode(64))
    text = db.Column(db.UnicodeText)

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

# Customized admin interface
class PageAdmin(sqla.ModelView):
    form_overrides = dict(text=CKTextAreaField)
    create_template = 'edit.html'
    edit_template = 'edit.html'
        
# Flask views
@app.route('/')
def index():
    return '<a href="/admin/">Click me to get to Admin!</a>'

@app.route('/ue_autocomplete', methods=['GET'])
def ue_autocomplete():
    search = request.args.get('q')
    query = db.session.query(User.email).filter(User.email.like('%' + str(search) + '%'))
    results = [mv[0] for mv in query.all()]
    return jsonify(matching_results=results)
    

if __name__ == '__main__':
    # Create admin
    admin = admin.Admin(app, name="Example: WYSIWYG" , template_mode='bootstrap3')
    #admin = admin.Admin(app, name='Select - from Local list', template_mode='bootstrap3')

    # Add views
    admin.add_view(PageAdmin(Page, db.session))
    # Create DB
    db.create_all()
    # Start app
    app.run(debug=True)
