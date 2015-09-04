import MySQLdb

html = """
<html>
   <head>
   <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
   <title>%s</title>
   </head>
   <body>%s</body>
</html>"""

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

   title = "MySQL Sample"
   body = "<table>"

   for row in data:
      fname = row[1]
      lname = row[2]
      body += "<tr><td>%s</td><td>%s</td></tr>" % (fname, lname)
   body += "</table>"

   response_body = html % (title, body)

   status = '200 OK'

   response_headers = [('Content-Type', 'text/html'),
                  ('Content-Length', str(len(response_body)))]
   start_response(status, response_headers)

   return [response_body]
