from . import *

# Flask routes
@app.route('/')
def index():
    return render_template('index.html')
