import os
import MySQLdb
import jinja2
import json

# This is our application object. It could have any name,
# except when using mod_wsgi where it must be "application"
def application(environ, start_response):

   # Open database connection
   db = MySQLdb.connect(user = "root", passwd = "o@bit837", db = "python", host = "127.0.0.1")

   # prepare a cursor object using cursor() method
   # and import a MySQL table as a dictionary
   cursor = db.cursor(MySQLdb.cursors.DictCursor)

   # execute SQL query using execute() method.
   cursor.execute("SELECT user_id, first_name, last_name, address, DATE_FORMAT(created_on, '%Y-%m-%d %H:%i:%S') as created_on, DATE_FORMAT(updated_on, '%Y-%m-%d %H:%i:%S') as updated_on FROM users")

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

   # Python json.
   page = {
      'title': 'Jinja Example Page',
      'users': data,
      'description': 'This is an example page created using Jinja2 with a JSON template.'
   }

   """
   JSON syntax is not Python syntax. JSON requires double quotes for its strings.
   You can dump JSON with double quote by:

   json_string = json.dumps(page)

   However, jinja2 cannot parse json. it takes python objects of any form as arguments (a list of dictionaries in your case).
   but you have to convert the json string to that first. that's what the json module does for you
   (one visible conversion here is that hte json string 'null' is mapped to the python None).

   json_python = json.loads(json_string)
   """

   parsed_template = template.render(title = "Country list", page = page)

   # The line response_body = parsed_template % (title = "Country list", users = data) shouldn't be here
   # - the call to template.render should have already generated a string with {{title}} and {{users}} replaced.
   response_body =  parsed_template.encode('utf-8')

   status = '200 OK'

   response_headers = [('Content-Type', 'text/html'),
               ('Content-Length', str(len(response_body)))]
   start_response(status, response_headers)

   return [response_body]
