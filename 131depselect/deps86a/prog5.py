'''
depselect
'''
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import flask_admin as admin
from flask_admin.contrib import sqla

app = Flask(__name__)
app.config['SECRET_KEY'] = '1234567901'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fground.sqlite'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)

# Flask views
@app.route('/')
def index():
    return '<a href="/admin/">Click me to get to Admin!</a>'

class Matriline(db.Model):
    __tablename__ = 'matriline'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode(64))
    pod_id = db.Column(db.Integer, db.ForeignKey('pod.id'))

    def __unicode__(self):
        return self.name

class Pod(db.Model):
    __tablename__ = 'pod'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode(64))
    matrilines = db.relationship('Matriline', backref='pod', lazy='select')
    clan_id = db.Column(db.Integer, db.ForeignKey('clan.id'))

    def __unicode__(self):
        return self.name

class Clan(db.Model):
    __tablename__ = 'clan'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode(64))
    pods = db.relationship('Pod', backref='clan', lazy='select')

    def __unicode__(self):
        return self.name

from flask_admin.contrib import sqla
from wtforms import SelectField
from flask.ext.admin.form import Select2Widget

class MatrilineView(sqla.ModelView):

    '''
    column_hide_backrefs = False
    form_extra_fields = {
        'clan': sqla.fields.QuerySelectField(
            label='Clan',
            query_factory=lambda: Clan.query.all,
            widget=Select2Widget()
        )
    }
    column_list = ('name', 'pod', 'clan')
    '''

# Create admin
admin = admin.Admin(app, name='db-simple', template_mode='bootstrap3')
admin.add_view(MatrilineView(Matriline, db.session))

if __name__ == '__main__':
    # Create DB
    db.create_all()
    # Start app
    app.run(host='0.0.0.0', port=5000, debug=True)

    