#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''
do this...
http://stackoverflow.com/questions/26684029/select2-field-implementation-in-flask-flask-admin

ref.
http://stackoverflow.com/questions/16160507/flask-admin-not-showing-foreignkey-columns
'''
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import flask_admin as admin
from flask_admin.contrib import sqla
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import column_property
from flask_admin.contrib.sqla import ModelView
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy import Column, ForeignKey, Integer, String, Table, Text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from flask_admin.form.widgets import Select2Widget

# Create application
app = Flask(__name__)
# Create dummy secrey key so we can use sessions
app.config['SECRET_KEY'] = '12344567901'
# define db engine..
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.sqlite'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#connect and  reflect...
connection = db.engine.connect()
# no need to reflect view...
db.metadata.reflect(bind=db.engine, only=['users'])
# from sqlacodegen, for order and person... 
Base = declarative_base()
meta = Base.metadata
 
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 
class Order(Base):
    __tablename__ = 'Orders'

    O_Id = Column(Integer, primary_key=True)
    OrderNo = Column(Integer, nullable=False)
    P_Id = Column(Integer)
    Name_fnln = Column(Text, nullable=False)

    Person = relationship(u'Person')

class Person(Base):
    __tablename__ = 'Persons'

    P_Id = Column(Integer, nullable=False)
    Name_fnln = Column(String(255), primary_key=True)
    donotuse_FirstName = Column(String(255))
    Address = Column(String(255))
    City = Column(String(255))
    
    def __unicode__(self):
        return self.Name_fnln
        
#reflect table...   
class users(db.Model):
    __table__ = db.Table(
        'users', db.metadata,
        #db.Column('id', db.Integer, primary_key=True),
        autoload=True,
        autoload_with=db.engine
    )
  
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Flask views
@app.route('/')
def index():
    return '<a href="/admin/">Click me to get to Admin!</a>'

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# customize views..
class dgview(sqla.ModelView):
    column_display_pk = True
   
    name= QuerySelectField(query_factory=lambda: models.User.query.all(),
                           widget=Select2Widget())

class Personview(sqla.ModelView):
    column_display_pk = True
  
    Name_fnln= QuerySelectField(query_factory=lambda: models.User.query.all(),
                           widget=Select2Widget())

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 
# Create admin
admin = admin.Admin(app, name='fltg 8select', template_mode='bootstrap3')

admin.add_view(dgview(users, db.session))
admin.add_view(Personview(Person, db.session))
admin.add_view(dgview(Order, db.session))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

if __name__ == '__main__':

    # Start app
    app.run(host='0.0.0.0', port=5000, debug=True)
    
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
