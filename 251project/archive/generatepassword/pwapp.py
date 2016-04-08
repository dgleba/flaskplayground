from project import app
from project import build_sample_db
import os

if __name__ == '__main__':

    # Build a sample db on the fly, if one does not exist yet.
    app_dir = os.path.realpath(os.path.dirname(__file__))
    proj_dir = 'project'
    database_path = os.path.join(app_dir, proj_dir, app.config['DATABASE_FILE'])
    if not os.path.exists(database_path):
        build_sample_db()
    app.run(host='0.0.0.0', port=5000, debug=True)
