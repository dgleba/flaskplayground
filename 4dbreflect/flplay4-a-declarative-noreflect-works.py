#
# simple db sqla app. use this as a base for db testing. 2016-02-10. David Gleba
#

'''

this is declarative from this page..

http://flask.pocoo.org/docs/0.10/patterns/sqlalchemy/

works

'''

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import flask_admin as admin
from flask_admin.contrib import sqla

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base


# Create application
app = Flask(__name__)

# Create dummy secrey key so we can use sessions
app.config['SECRET_KEY'] = '1234567901asdfafafaee'

# Create in-memory database
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sample_db_2.sqlite'
#app.config['SQLALCHEMY_ECHO'] = True
#db = SQLAlchemy(app)


engine = create_engine('sqlite:///test.sqlite', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    #import yourapplication.models
    Base.metadata.create_all(bind=engine)
    
#from yourapplication.database import db_session

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


from sqlalchemy import Column, Integer, String
#from yourapplication.database import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    email = Column(String(120), unique=True)

    def __init__(self, name=None, email=None):
        self.name = name
        self.email = email

    def __repr__(self):
        return '<User %r>' % (self.name)
        
        
    
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# Flask views
@app.route('/')
def index():
    return '<a href="/admin/">Click me to get to Admin!</a>'

    
'''
class Car(db.Model):
    __tablename__ = 'cars'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    desc = db.Column(db.String(50))

    def __unicode__(self):
        return self.desc

class Tyre(db.Model):
    __tablename__ = 'tyres'
    car_id = db.Column(db.Integer, db.ForeignKey('cars.id'), primary_key=True)
    tyre_id = db.Column(db.Integer, primary_key=True)
    car = db.relationship('Car', backref='tyres')
    desc = db.Column(db.String(50))

class CarAdmin(sqla.ModelView):
    column_display_pk = True
    form_columns = ['id', 'desc']

class TyreAdmin(sqla.ModelView):
    column_display_pk = True
    form_columns = ['car', 'tyre_id', 'desc']

# Create admin
admin = admin.Admin(app, name='db-4-reflect', template_mode='bootstrap3')
admin.add_view(CarAdmin(Car, db.session))
admin.add_view(TyreAdmin(Tyre, db.session))
'''

class dgcUserAdmin(sqla.ModelView):
    column_display_pk = True

# Create admin
admin = admin.Admin(app, name='db-4-reflect', template_mode='bootstrap3')
admin.add_view(dgcUserAdmin(User, db_session))


if __name__ == '__main__':

    # Create DB
    #db.create_all()
    
    #from yourapplication.database import init_db
    init_db()

    '''
    u = User('admin', 'admin@localhost')
    db_session.add(u)
    db_session.commit()
    '''
    

    # Start app
    app.run(host='0.0.0.0', port=5000, debug=True)
