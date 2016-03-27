'''
this works.

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

#secrets...
import creds
app.config.from_pyfile('creds.py')

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

from flask.ext.mail import Message, Mail
mail = Mail()
app.config["MAIL_SERVER"] = "smtp.live.com"
app.config["MAIL_PORT"] = 587
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USERNAME"] = creds.cred['mailu']
app.config["MAIL_PASSWORD"] = creds.cred['mailpass']
mail.init_app(app)
    
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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

# look at the ideas here to seperate the email into a template... http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xi-email-support

    @action('mail1', 'Mail1', 'Are you sure you want to mail selected record?')
    def action_mail1(self, ids):
        try:
            # if more than one row is selected, show error and don't mail anything..
            totalcount = User.query.filter(User.id.in_(ids)).count()
            print 'totalcount= ', totalcount
            if totalcount > 1:
                flash('Error!  Only select one row to email to the group!'  )
                return
            
            # Mail the one record.
            query = User.query.filter(User.id.in_(ids))
            count = 0
            for user in query.all():
                msg = Message('test-sendmail1-9-f-20160314', sender=creds.cred['mailu'], recipients=['dgleba@gmail.com'])
                msg.body = """
                From: %s <%s>
                user name: %s 
                """ % ('dave', creds.cred['mailu'], user.last_name)
                msg.html = '''
                From: %s <%s>
                <table cellpadding="5" cellspacing="0" border="1"   bgcolor="#DAFFDA">
                <tr ><td>last name: </td><td> %s </td></tr>
                </table>
                '''  %('dave', creds.cred['mailu'], user.last_name)
                mail.send(msg)
                #return ('<br><br><hr> Mail send processed. Press your browser BACK button.<hr>')
                count += 1

            flash('Mail was successfully sent.  '  )
        
        except Exception as ex:
            if not self.handle_view_exception(ex):
                raise

            flash(gettext('Failed . %(error)s', error=str(ex)), 'error')        
    
    
# Flask views
@app.route('/')
def index():
    return '<a href="/admin/">Click me to get to Admin!</a>'

if __name__ == '__main__':
    admin = admin.Admin(app, name="Batch-action" , template_mode='bootstrap3')
    admin.add_view(UserView(User, db.session))
    db.create_all()
    app.run(debug=True)
