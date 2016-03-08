# Small-Example: form data written to database. David Gleba.

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import flask_admin as admin
from flask_admin.contrib import sqla
#from wtforms import SelectField
#from functools import wraps
from flask import request, Blueprint, render_template, jsonify, flash, \
    redirect, url_for

app = Flask(__name__)  # Create application
app.config['SECRET_KEY'] = '123456790'  # Create dummy secrey key so we can use sessions
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fground.sqlite' # Create database
db = SQLAlchemy(app)

@app.route('/')  # Flask views
def index():
    return '''
    <a href="/admin/">Click me to get to Admin!</a>
    </br></br>
    <a href="/pcr">Click me to create a product</a>
    '''
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    price = db.Column(db.Float)
    category_id = db.Column(db.Integer)

    def __init__(self, name, price, category_id):
        self.name = name
        self.price = price
        self.category_id = category_id

    def __repr__(self):
        return '<Product %d>' % self.id

@app.route('/pcr', methods=['GET', 'POST'])
def create_product():
    if request.method == 'POST':
        name = request.form.get('name')
        price = request.form.get('price')
        category_id = request.form.get('category')
        product = Product(name, price, category_id)
        db.session.add(product)
        db.session.commit()
        flash('The product %s has been created' % name, 'success')
        return redirect(url_for('create_product', id=product.id))
    return render_template('product-create.html')
    
# Create admin
admin = admin.Admin(app, name='Select - from Local list', template_mode='bootstrap3')
admin.add_view(sqla.ModelView(Product, db.session))

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
