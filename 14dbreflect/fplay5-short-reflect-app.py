''' short app to reflect a table . Uses declarative reflect.
'''
from flask import Flask
from flask_admin.contrib import sqla
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import scoped_session, sessionmaker, create_session, column_property
import flask_admin as admin

# Create application
app = Flask(__name__)
app.config['SECRET_KEY'] = '12345679'
engine = create_engine('sqlite:///test.sqlite', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()
metadata = MetaData(bind=engine)

def init_db():
    Base.metadata.create_all(bind=engine)

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

# reflect users table..
class User(Base):
    __table__ = Table('users', metadata, autoload=True)
 
# Flask views
@app.route('/')
def index():
    return '<a href="/admin/">Click me to get to Admin!</a>'

# Create admin
admin = admin.Admin(app, name='db-4-reflect', template_mode='bootstrap3')
admin.add_view(sqla.ModelView(User, db_session))

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000, debug=True)
