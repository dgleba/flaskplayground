# full gist: please run this
# http://stackoverflow.com/questions/33660840/flask-admin-form-constrain-value-of-field-2-depending-on-value-of-field-1

from flask import Flask
from flask_admin import Admin
from flask_admin.contrib import sqla
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

# Create application
app = Flask(__name__)

# Create dummy secrey key so we can use sessions
app.config['SECRET_KEY'] = '123456790'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///a_sample_database.sqlite'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)


# Flask views
@app.route('/')
def index():
    return '<a href="/admin/">Click me to get to Admin!</a>'


class Method(db.Model):
    __tablename__ = 'method'
    mid = Column(Integer, primary_key=True)
    method = Column(String(20), nullable=False, unique=True)
    methodarg = relationship('MethodArg', backref='method')
    recipe = relationship('Recipe', backref='method')


    def __str__(self):
        return self.method


class MethodArg(db.Model):
    __tablename__ = 'methodarg'
    maid = Column(Integer, primary_key=True)
    mid = Column(ForeignKey('method.mid', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    methodarg = Column(String(20), nullable=False, unique=True)
    recipearg = relationship('RecipeArg', backref='methodarg')
    inline_models = (Method,)


    def __str__(self):
        return self.methodarg


class Recipe(db.Model):
    __tablename__ = 'recipe'
    rid = Column(Integer, primary_key=True)
    mid = Column(ForeignKey('method.mid', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    recipe = Column(String(20), nullable=False, index=True)
    recipearg = relationship('RecipeArg', backref='recipe')
    inline_models = (Method,)

    def __str__(self):
        return self.recipe


class RecipeArg(db.Model):
    __tablename__ = 'recipearg'

    raid = Column(Integer, primary_key=True)
    rid = Column(ForeignKey('recipe.rid', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    maid = Column(ForeignKey('methodarg.maid', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    strvalue = Column(String(80), nullable=False)
    inline_models = (Recipe, MethodArg)


    def __str__(self):
        return self.strvalue


class MethodArgAdmin(sqla.ModelView):
    column_list = ('method', 'methodarg')
    column_editable_list = column_list



class RecipeAdmin(sqla.ModelView):
    column_list = ('recipe', 'method')
    column_editable_list = column_list



class RecipeArgAdmin(sqla.ModelView):
    column_list = ('recipe', 'methodarg', 'strvalue')
    column_editable_list = column_list


# Create admin app
admin = Admin(app, name="Constrain Values", template_mode='bootstrap3')
admin.add_view(RecipeArgAdmin(RecipeArg, db.session))
# More submenu
admin.add_view(sqla.ModelView(Method, db.session, category='See Other Tables'))
admin.add_view(MethodArgAdmin(MethodArg, db.session, category='See Other Tables'))
admin.add_view(RecipeAdmin(Recipe, db.session, category='See Other Tables'))


if __name__ == '__main__':

    db.drop_all()
    db.create_all()
    db.session.add(Method(mid=1, method='tabulate_results'))
    db.session.add(Method(mid=2, method='pretty_print'))
    db.session.commit()
    db.session.add(MethodArg(maid=1, mid=1, methodarg='rows'))
    db.session.add(MethodArg(maid=2, mid=1, methodarg='display_total'))
    db.session.add(MethodArg(maid=3, mid=2, methodarg='embellishment_character'))
    db.session.add(MethodArg(maid=4, mid=2, methodarg='lines_to_jump'))
    db.session.add(Recipe(rid=1, mid=1, recipe='Serious Report'))
    db.session.add(Recipe(rid=2, mid=2, recipe='ASCII Art'))
    db.session.commit()
    db.session.add(RecipeArg(raid=1, rid=1, maid=2, strvalue='true' ))
    db.session.add(RecipeArg(raid=2, rid=1, maid=1, strvalue='12' ))
    db.session.add(RecipeArg(raid=3, rid=2, maid=4, strvalue='3' ))
    db.session.commit()

    # Start app
    app.run(debug=True)
    