#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''
reflect a view . 2016-02-11. David Gleba

based on 
  3dbsimple,
  https://gist.github.com/nickretallack/7552307

'''

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import flask_admin as admin
from flask_admin.contrib import sqla

# Create application
app = Flask(__name__)

# Create dummy secrey key so we can use sessions
app.config['SECRET_KEY'] = '12344567901'

# Create 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.sqlite'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#connect and  reflect...
connection = db.engine.connect()
db.metadata.reflect(bind=db.engine)
    
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# reflect view...
class vw_user1(db.Model):
    __table__ = db.Table(
        'vw_user1', db.metadata,
        db.Column('id', db.Integer, primary_key=True),
        #...other column defs...
        autoload=True,
        autoload_with=db.engine
    )
       
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
# Flask views
@app.route('/')
def index():
    return '<a href="/admin/">Click me to get to Admin!</a>'


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
   
class vwuser_view(sqla.ModelView):
    column_display_pk = True
    
    
# Create admin
admin = admin.Admin(app, name='flpg6 reflect view', template_mode='bootstrap3')
#admin.add_view(CarAdmin(Car, db.session))
#admin.add_view(TyreAdmin(Tyre, db.session))
admin.add_view(vwuser_view(vw_user1, db.session))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

if __name__ == '__main__':

    # Create DB
    #db.create_all()

    # Start app
    app.run(host='0.0.0.0', port=5000, debug=True)
    
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
