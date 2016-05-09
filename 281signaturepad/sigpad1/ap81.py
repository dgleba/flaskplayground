'''
https://github.com/thomasjbradley/signature-pad/blob/gh-pages/examples/require-drawn-signature.html

https://github.com/thomasjbradley/signature-pad/blob/gh-pages/documentation.md

'''
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from wtforms import fields, widgets, HiddenField
import flask_admin as admin
from flask_admin.contrib import sqla
from flask_admin.form import rules

# Create application
app = Flask(__name__)
app.config['SECRET_KEY'] = '123456790'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sample_db.sqlite'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)

# Model
class Page(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name1 = db.Column(db.Unicode(64))
    output = db.Column(db.UnicodeText)

    def __unicode__(self):
        return self.name1

# Customized admin interface
class PageAdmin(sqla.ModelView):

    '''form_overrides = {
      'output': HiddenField,
    }'''

    '''Add html for signature pad after name1...
    '''
    form_create_rules = ('name1', rules.HTML('''
    <p class="drawItDesc">Draw your signature</p>
    <ul class="sigNav">
      <li class="drawIt"><a href="#draw-it" >Draw It</a></li>
      <li class="clearButton"><a href="#clear">Clear</a></li>
    </ul>
    <div class="sig sigWrapper">
      <div class="typed"></div>
      <canvas class="pad" width="298" height="55"></canvas>
      <input type="hidden" name="output" class="output">
    </div><br>
    '''), )
    
    create_template = 'create.html'
    edit_template = 'edit.html'
    action_disallowed_list = ('delete')
     
    
# Flask views
@app.route('/')
def index():
    return '<a style="font-size:3em;" , href="/admin/">Click me to get to Admin!</a>'

if __name__ == '__main__':
    # Create admin
    admin = admin.Admin(app, name="signature-pad")
    admin.add_view(PageAdmin(Page, db.session))
    db.create_all()
    app.run(debug=True)
