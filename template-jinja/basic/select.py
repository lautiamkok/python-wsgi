import os
import MySQLdb
import jinja2

# This is our application object. It could have any name,
# except when using mod_wsgi where it must be "application"
def application(environ, start_response):

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
   TEMPLATE_FILE = "page.html"

   # Read the template file using the environment object.
   # This also constructs our Template object.
   template = JINJA_ENVIRONMENT.get_template(TEMPLATE_FILE)

   parsed_template = template.render(title = "Country list", users = data)
   #print data
   #print parsed_template

   # The line response_body = parsed_template % (title = "Country list", users = data) shouldn't be here
   # - the call to template.render should have already generated a string with {{title}} and {{users}} replaced.
   response_body =  parsed_template.encode('utf-8')

   status = '200 OK'

   response_headers = [('Content-Type', 'text/html'),
               ('Content-Length', str(len(response_body)))]
   start_response(status, response_headers)

   return [response_body]
