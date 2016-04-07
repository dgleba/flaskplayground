'''
Small-Example: email is shown as a link to the edit view of the record.
    http://stackoverflow.com/questions/17174707/can-model-views-in-flask-admin-hyperlink-to-other-model-views
'''
from flask import Flask, Markup, url_for
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
   
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    def __str__(self):
        return self.email
        
class uAdmin(sqla.ModelView):
    def _user_formatter(view, context, model, name):
        return Markup(
            "<a href='%s'>%s</a>" % (
                url_for('user.edit_view', id=model.id),
                model.email
            )
        ) if model.email else ""

    column_formatters = {
        'email': _user_formatter
    }
    
# Create admin
admin = admin.Admin(app, name='Make cell into a link', template_mode='bootstrap3')
admin.add_view(uAdmin(User, db.session))

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
