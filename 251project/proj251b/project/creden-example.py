
# credentials not publicly shared. Exclude this from git repository.

# Create dummy secret key so we can use sessions
SECRET_KEY = '1234567890'

# Create  database
DATABASE_FILE = 'fground.sqlite'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE_FILE

SECURITY_PASSWORD_SALT = "random-salt-string"
