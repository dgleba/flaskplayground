~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Title:  .
-----------------------2016-03-05[Mar-Sat]16-03PM

flask --app=flaskr initdb

got error

    @app.cli.command('initdb')
AttributeError: 'Flask' object has no attribute 'cli'


had to run

pip install https://github.com/mitsuhiko/flask/tarball/master

this now has the flask command.


https://github.com/mitsuhiko/flask/issues/1048

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

