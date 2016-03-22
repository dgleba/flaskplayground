from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'  #absolute path
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.sqlite'
db = SQLAlchemy(app)

app.secret_key = 'some_random_key'

from my_app.catalog.views import catalog
app.register_blueprint(catalog)

db.create_all()
