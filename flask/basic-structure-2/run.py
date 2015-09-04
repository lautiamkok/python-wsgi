import os
import sys
from flask import Flask

# Flask defaults to the 'templates' and 'static' folders at the root path of the application.
project_root = os.path.dirname(__file__)
template_path = os.path.join(project_root, 'app/templates')
static_path = os.path.join(project_root, 'app/static')

flaskapp = Flask(__name__, template_folder=template_path, static_folder=static_path)

from app import routes

if __name__ == '__main__':
    flaskapp.run(debug = True)
