from . import *

# Flask views
@app.route('/')
def index():
    return render_template('index.html')
