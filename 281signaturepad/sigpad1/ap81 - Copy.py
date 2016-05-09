from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from wtforms import fields, widgets
import flask_admin as admin
from flask_admin.contrib import sqla
from flask_admin.form import rules

# Create application
app = Flask(__name__)
app.config['SECRET_KEY'] = '123456790'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sample_db.sqlite'
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
        kwargs['class'] = u'%s %s' % (existing_classes, "sig sigWrapper")
        return super(CKTextAreaWidget, self).__call__(field, **kwargs)

class CKTextAreaField(fields.TextAreaField):
    widget = CKTextAreaWidget()

# Model
class Page(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name1 = db.Column(db.Unicode(64))
    text1 = db.Column(db.UnicodeText)
    output = db.Column(db.UnicodeText)

    def __unicode__(self):
        return self.name1

# Customized admin interface
class PageAdmin(sqla.ModelView):
    form_overrides = dict(text1=CKTextAreaField)

    form_create_rules = ('name1','text1', rules.HTML('''
    <p class="drawItDesc">Draw your signature</p>
    <ul class="sigNav">
      <li class="drawIt"><a href="#draw-it" >Draw It</a></li>
      <li class="clearButton"><a href="#clear">Clear</a></li>
    </ul>
    <div class="sig sigWrapper">
      <div class="typed"></div>
      <canvas class="pad" width="198" height="55"></canvas> 
          
    '''), 'output', rules.HTML('</div>'))
    
    create_template = 'create.html'
    edit_template = 'edit.html'

     
    
# Flask views
@app.route('/')
def index():
    return '<a style="font-size:3em;" , href="/admin/">Click me to get to Admin!</a>'

if __name__ == '__main__':
    # Create admin
    admin = admin.Admin(app, name="Example: WYSIWYG")
    admin.add_view(PageAdmin(Page, db.session))
    db.create_all()
    app.run(debug=True)
