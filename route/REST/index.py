import os
import MySQLdb
import jinja2

# Setup a mapper
from routes import Mapper

map = Mapper()
#map.resource("user", "users")

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

   # Set parameters for the function.
   parameters = {'mapped': mapped }

   print mapped

   if mapped == None:
      response_body =  """
        <html>
         <head><title>404 Not Found</title></head>
         <body>
          <h1>404 Not Found</h1>
          The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.
         </body>
        </html>"""
      status = '404 Not Found'

   else:

      # Everything done, return the response.
      response_body =  function_list[mapped['controller']](**parameters)
      status = '200 OK'

   response_headers = [('Content-Type', 'text/html'),
                       ('Content-Length', str(len(response_body)))]

   start_response(status, response_headers)

   return [response_body]

def main(mapped = ""):

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

def addUser(mapped = ""):

   templateLoader = jinja2.FileSystemLoader(searchpath = os.path.dirname(__file__) + "/template/")

   JINJA_ENVIRONMENT = jinja2.Environment(loader = templateLoader)

   # This constant string specifies the template file we will use.
   TEMPLATE_FILE = "add.html"

   template = JINJA_ENVIRONMENT.get_template(TEMPLATE_FILE)

   parsed_template = template.render(title = "Add User")

   response_body =  parsed_template.encode('utf-8')

   return response_body

def updateUser(mapped = ""):

   templateLoader = jinja2.FileSystemLoader(searchpath = os.path.dirname(__file__) + "/template/")

   JINJA_ENVIRONMENT = jinja2.Environment(loader = templateLoader)

   TEMPLATE_FILE = "update.html"

   template = JINJA_ENVIRONMENT.get_template(TEMPLATE_FILE)

   parsed_template = template.render(title = "Update User", id = mapped['id'])

   response_body =  parsed_template.encode('utf-8')

   return response_body

def postUser(mapped = ""):

   templateLoader = jinja2.FileSystemLoader(searchpath = os.path.dirname(__file__) + "/template/")

   JINJA_ENVIRONMENT = jinja2.Environment(loader = templateLoader)

   TEMPLATE_FILE = "post.html"

   template = JINJA_ENVIRONMENT.get_template(TEMPLATE_FILE)

   parsed_template = template.render(title = "Added User")

   response_body =  parsed_template.encode('utf-8')

   return response_body

def putUser(mapped = ""):

   templateLoader = jinja2.FileSystemLoader(searchpath = os.path.dirname(__file__) + "/template/")

   JINJA_ENVIRONMENT = jinja2.Environment(loader = templateLoader)

   TEMPLATE_FILE = "put.html"

   template = JINJA_ENVIRONMENT.get_template(TEMPLATE_FILE)

   parsed_template = template.render(title = "PUT User", id = mapped['id'])

   response_body =  parsed_template.encode('utf-8')

   return response_body

def deleteUser(mapped = ""):

   templateLoader = jinja2.FileSystemLoader(searchpath = os.path.dirname(__file__) + "/template/")

   JINJA_ENVIRONMENT = jinja2.Environment(loader = templateLoader)

   TEMPLATE_FILE = "delete.html"

   template = JINJA_ENVIRONMENT.get_template(TEMPLATE_FILE)

   parsed_template = template.render(title = "Delete User", id = mapped['id'])

   response_body =  parsed_template.encode('utf-8')

   return response_body

function_list = {
   'main' : main,
   'addUser' : addUser,
   'updateUser' : updateUser,
   'postUser' : postUser,
   'putUser' : putUser,
   'deleteUser' : deleteUser
}

from paste.exceptions.errormiddleware import ErrorMiddleware
application = ErrorMiddleware(application, debug=True)
