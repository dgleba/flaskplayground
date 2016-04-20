
# http://stackoverflow.com/questions/5055042/whats-the-best-practice-using-a-settings-file-in-python

SQLALCHEMY_ECHO = True

# Flask-Security config
SECURITY_URL_PREFIX = "/admin"

# http://stackoverflow.com/questions/30827696/flask-security-login-via-username-and-not-email
SECURITY_USER_IDENTITY_ATTRIBUTES = 'username'

# Flask-Security URLs, overridden because they don't put a / at the end
SECURITY_LOGIN_URL = "/login/"
SECURITY_LOGOUT_URL = "/logout/"
SECURITY_REGISTER_URL = "/register/"

SECURITY_POST_LOGIN_VIEW = "/admin/"
SECURITY_POST_LOGOUT_VIEW = "/admin/"
SECURITY_POST_REGISTER_VIEW = "/admin/"

# Flask-Security features
SECURITY_REGISTERABLE = True
SECURITY_SEND_REGISTER_EMAIL = False