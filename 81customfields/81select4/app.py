from flask import Flask, render_template, url_for, request, abort, json, Response
from flask.ext.admin import Admin, BaseView, expose, babel
from flask.ext.admin.contrib.sqla.ajax import QueryAjaxModelLoader
from flask.ext.admin.model.fields import AjaxSelectField, AjaxSelectMultipleField
from flask.ext.sqlalchemy import SQLAlchemy
from wtforms import Form
from faker import Factory

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'super-secret'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fground.sqlite'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)

try:
    from flask_debugtoolbar import DebugToolbarExtension
    DebugToolbarExtension(app)
except:
    pass


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)

    first_name = db.Column(db.Unicode(length=255), nullable=False)
    last_name = db.Column(db.Unicode(length=255), nullable=False)
    email = db.Column(db.Unicode(length=254), nullable=False, unique=True)

    def __unicode__(self):
        return u"{first} {last}; {email}".format(first=self.first_name, last=self.last_name, email=self.email)


def get_loader_by_name(name):
    _dicts = {
        'user': QueryAjaxModelLoader(
            'user',
            db.session, User,
            fields=['first_name', 'last_name', 'email'],
            page_size=10,
            placeholder="Select a user"
        )
    }
    return _dicts.get(name, None)


class TestView(BaseView):

    def __init__(self, name=None, category=None,
                 endpoint=None, url=None,
                 template='admin/index.html',
                 menu_class_name=None,
                 menu_icon_type=None,
                 menu_icon_value=None):
        super(TestView, self).__init__(name or babel.lazy_gettext('Home'),
                                             category,
                                             endpoint or 'admin',
                                             url or '/admin',
                                             'static',
                                             menu_class_name=menu_class_name,
                                             menu_icon_type=menu_icon_type,
                                             menu_icon_value=menu_icon_value)
        self._template = template

    @expose('/', methods=('GET',))
    def index_view(self):
        _form = TestForm()
        return self.render(self._template, form=_form)

    @expose('/', methods=('POST',))
    def post_view(self):
        pass

    @expose('/ajax/lookup/')
    def ajax_lookup(self):
        name = request.args.get('name')
        query = request.args.get('query')
        offset = request.args.get('offset', type=int)
        limit = request.args.get('limit', 10, type=int)

        loader = get_loader_by_name(name)

        if not loader:
            abort(404)

        data = [loader.format(m) for m in loader.get_list(query, offset, limit)]
        return Response(json.dumps(data), mimetype='application/json')

# Create admin and Test View
admin = Admin(app, name='Admin', template_mode='bootstrap3')
admin.add_view(TestView(template='test.html', name="Test", url='/test', endpoint='test'))


class TestForm(Form):

    single_user = AjaxSelectField(
        loader=get_loader_by_name('user')
    )

    multiple_users = AjaxSelectMultipleField(
        loader=get_loader_by_name('user')
    )


@app.route('/')
def index():
    return render_template("index.html", link=url_for('test.index_view'))


def build_db():

    #db.drop_all()
    db.create_all()
    fake = Factory.create()
    for index in range(0, 100):
        _first_name = fake.first_name()
        _last_name = fake.last_name()
        _user_db = User(
            first_name=_first_name,
            last_name=_last_name,
            email="{first}.{last}{index}@example.com".format(first=_first_name.lower(), last=_last_name.lower(), index=index)
        )
        db.session.add(_user_db)

    db.session.commit()


@app.before_first_request
def before_first_request():
    #build_db()
    return(0)

if __name__ == '__main__':
    app.debug = True
    app.run(port=5000, debug=True)