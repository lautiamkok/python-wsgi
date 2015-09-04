import os
import MySQLdb
import jinja2

# Setup a mapper
from routes import Mapper
map = Mapper()
map.resource("user", "users")

map.connect("add user", "/user",
   controller = "addUser",
   action = "add",
   conditions = dict(method = ["GET"])
)

map.connect("post user", "/user",
   controller = "postUser",
   action = "post",
   conditions = dict(method = ["POST"])
)

map.connect("update user", "/user/{id}",
   controller = "updateUser",
   action = "update",
   conditions = dict(method = ["GET"])
)

map.connect("put user", "/user/{id}",
   controller = "putUser",
   action = "put",
   conditions = dict(method = ["PUT"])
)

map.connect("delete user", "/user/{id}",
   controller = "deleteUser",
   action = "delete",
   conditions = dict(method = ["DELETE"])
)

map.connect("home", "/",
   controller = "main",
   action = "index",
   conditions = dict(method = ["GET"])
)

# This is our application object. It could have any name,
# except when using mod_wsgi where it must be "application"
def application(environ, start_response):

   # Get the request path info.
   uri = environ.get('PATH_INFO', '')
   path_info = uri if uri else '/'

   # Get the HTTP request method: PUT, GET, DELETE, POST.
   request_method = environ.get('REQUEST_METHOD', '')
   map.environ = {'REQUEST_METHOD': request_method}

   # Match a URL, returns a dict or None if no match
   mapped = map.match(path_info)

   # Everything done, return the response:
   if mapped['action'] == 'index' :
      response_body = index(environ, start_response, mapped)
   elif mapped['action'] == 'add':
      response_body = add(environ, start_response, mapped)
   elif mapped['action'] == 'update':
      response_body = update(environ, start_response, mapped)
   elif mapped['action'] == 'post':
      response_body = post(environ, start_response, mapped)
   elif mapped['action'] == 'put':
      response_body = put(environ, start_response, mapped)
   elif mapped['action'] == 'delete':
      response_body = delete(environ, start_response, mapped)
   else:
      response_body =  "Not exist."

   status = '200 OK'

   response_headers = [('Content-Type', 'text/html'),
               ('Content-Length', str(len(response_body)))]
   start_response(status, response_headers)

   return [response_body]

def index(environ, start_response, mapped):

   # Open database connection
   #db = MySQLdb.connect("127.0.0.1","root","o@bit837","python" )
   db = MySQLdb.connect(user = "root", passwd = "o@bit837", db = "python", host = "127.0.0.1")

   # prepare a cursor object using cursor() method
   cursor = db.cursor()

   # execute SQL query using execute() method.
   cursor.execute("SELECT * FROM users")

   # Fetch a single row using fetchone() method.
   data = cursor.fetchall()

   # disconnect from server
   cursor.close()
   db.close()

   # In this case, we will load templates off the filesystem.
   # This means we must construct a FileSystemLoader object.
   #
   # The search path can be used to make finding templates by
   #   relative paths much easier.  In this case, we are using
   #   absolute paths and thus set it to the filesystem root.
   templateLoader = jinja2.FileSystemLoader(searchpath = os.path.dirname(__file__) + "/template/")

   # An environment provides the data necessary to read and
   # parse our templates.  We pass in the loader object here.
   JINJA_ENVIRONMENT = jinja2.Environment(loader = templateLoader)

   # This constant string specifies the template file we will use.
   TEMPLATE_FILE = "home.html"

   # Read the template file using the environment object.
   # This also constructs our Template object.
   template = JINJA_ENVIRONMENT.get_template(TEMPLATE_FILE)

   parsed_template = template.render(title = "Country list", users = data)

   # The line response_body = parsed_template % (title = "Country list", users = data) shouldn't be here
   # - the call to template.render should have already generated a string with {{title}} and {{users}} replaced.
   response_body =  parsed_template.encode('utf-8')

   return response_body

def add(environ, start_response, mapped):

   # In this case, we will load templates off the filesystem.
   # This means we must construct a FileSystemLoader object.
   #
   # The search path can be used to make finding templates by
   #   relative paths much easier.  In this case, we are using
   #   absolute paths and thus set it to the filesystem root.
   templateLoader = jinja2.FileSystemLoader(searchpath = os.path.dirname(__file__) + "/template/")

   # An environment provides the data necessary to read and
   # parse our templates.  We pass in the loader object here.
   JINJA_ENVIRONMENT = jinja2.Environment(loader = templateLoader)

   # This constant string specifies the template file we will use.
   TEMPLATE_FILE = "add.html"

   # Read the template file using the environment object.
   # This also constructs our Template object.
   template = JINJA_ENVIRONMENT.get_template(TEMPLATE_FILE)

   parsed_template = template.render(title = "Add User")

   # The line response_body = parsed_template % (title = "Country list", users = data) shouldn't be here
   # - the call to template.render should have already generated a string with {{title}} and {{users}} replaced.
   response_body =  parsed_template.encode('utf-8')

   return response_body

def update(environ, start_response, mapped):

   # In this case, we will load templates off the filesystem.
   # This means we must construct a FileSystemLoader object.
   #
   # The search path can be used to make finding templates by
   #   relative paths much easier.  In this case, we are using
   #   absolute paths and thus set it to the filesystem root.
   templateLoader = jinja2.FileSystemLoader(searchpath = os.path.dirname(__file__) + "/template/")

   # An environment provides the data necessary to read and
   # parse our templates.  We pass in the loader object here.
   JINJA_ENVIRONMENT = jinja2.Environment(loader = templateLoader)

   # This constant string specifies the template file we will use.
   TEMPLATE_FILE = "update.html"

   # Read the template file using the environment object.
   # This also constructs our Template object.
   template = JINJA_ENVIRONMENT.get_template(TEMPLATE_FILE)

   parsed_template = template.render(title = "Update User", id = mapped['id'])

   # The line response_body = parsed_template % (title = "Country list", users = data) shouldn't be here
   # - the call to template.render should have already generated a string with {{title}} and {{users}} replaced.
   response_body =  parsed_template.encode('utf-8')

   return response_body

def post(environ, start_response, mapped):

   # In this case, we will load templates off the filesystem.
   # This means we must construct a FileSystemLoader object.
   #
   # The search path can be used to make finding templates by
   #   relative paths much easier.  In this case, we are using
   #   absolute paths and thus set it to the filesystem root.
   templateLoader = jinja2.FileSystemLoader(searchpath = os.path.dirname(__file__) + "/template/")

   # An environment provides the data necessary to read and
   # parse our templates.  We pass in the loader object here.
   JINJA_ENVIRONMENT = jinja2.Environment(loader = templateLoader)

   # This constant string specifies the template file we will use.
   TEMPLATE_FILE = "post.html"

   # Read the template file using the environment object.
   # This also constructs our Template object.
   template = JINJA_ENVIRONMENT.get_template(TEMPLATE_FILE)

   parsed_template = template.render(title = "Added User")

   # The line response_body = parsed_template % (title = "Country list", users = data) shouldn't be here
   # - the call to template.render should have already generated a string with {{title}} and {{users}} replaced.
   response_body =  parsed_template.encode('utf-8')

   return response_body

def put(environ, start_response, mapped):

   # In this case, we will load templates off the filesystem.
   # This means we must construct a FileSystemLoader object.
   #
   # The search path can be used to make finding templates by
   #   relative paths much easier.  In this case, we are using
   #   absolute paths and thus set it to the filesystem root.
   templateLoader = jinja2.FileSystemLoader(searchpath = os.path.dirname(__file__) + "/template/")

   # An environment provides the data necessary to read and
   # parse our templates.  We pass in the loader object here.
   JINJA_ENVIRONMENT = jinja2.Environment(loader = templateLoader)

   # This constant string specifies the template file we will use.
   TEMPLATE_FILE = "put.html"

   # Read the template file using the environment object.
   # This also constructs our Template object.
   template = JINJA_ENVIRONMENT.get_template(TEMPLATE_FILE)

   parsed_template = template.render(title = "PUT User", id = mapped['id'])

   # The line response_body = parsed_template % (title = "Country list", users = data) shouldn't be here
   # - the call to template.render should have already generated a string with {{title}} and {{users}} replaced.
   response_body =  parsed_template.encode('utf-8')

   return response_body

def delete(environ, start_response, mapped):

   # In this case, we will load templates off the filesystem.
   # This means we must construct a FileSystemLoader object.
   #
   # The search path can be used to make finding templates by
   #   relative paths much easier.  In this case, we are using
   #   absolute paths and thus set it to the filesystem root.
   templateLoader = jinja2.FileSystemLoader(searchpath = os.path.dirname(__file__) + "/template/")

   # An environment provides the data necessary to read and
   # parse our templates.  We pass in the loader object here.
   JINJA_ENVIRONMENT = jinja2.Environment(loader = templateLoader)

   # This constant string specifies the template file we will use.
   TEMPLATE_FILE = "delete.html"

   # Read the template file using the environment object.
   # This also constructs our Template object.
   template = JINJA_ENVIRONMENT.get_template(TEMPLATE_FILE)

   parsed_template = template.render(title = "Delete User", id = mapped['id'])

   # The line response_body = parsed_template % (title = "Country list", users = data) shouldn't be here
   # - the call to template.render should have already generated a string with {{title}} and {{users}} replaced.
   response_body =  parsed_template.encode('utf-8')

   return response_body

from paste.exceptions.errormiddleware import ErrorMiddleware
application = ErrorMiddleware(application, debug=True)
