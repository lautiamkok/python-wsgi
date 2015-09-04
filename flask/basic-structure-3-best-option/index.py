import os
import sys

# mod_wsgi likely doesn't know about your virtualenv, and simply needs to be told
# to use that rather than the default system environment.
activate_this = os.path.dirname(__file__) + '/venv/Scripts/activate_this.py'
exec(open(activate_this).read(), dict(__file__ = activate_this))

# Expand Python classes path with your app's path.
sys.path.insert(0, os.path.dirname(__file__) + '/app')

# Or:
#sys.path.append('C:/EasyPHP-DevServer/data/localweb/python-boilerplates/wsgi/flaskapp')

from routes import flaskapp

#Initialize WSGI app object.
application = flaskapp

# Or:
#from hello import app as application
