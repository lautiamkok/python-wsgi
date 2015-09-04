import datetime

html = """
<html>
   <head>
   <title>%s</title>
   </head>
   <body>%s</body>
</html>"""

# This is our application object. It could have any name,
# except when using mod_wsgi where it must be "application"
def application(environ, start_response):

   title = "Current time"
   body = "Current time is: "+ datetime.datetime.now().strftime( "%Y-%m-%d %H:%M:%S")

   response_body = html % (title, body)

   status = '200 OK'

   response_headers = [('Content-Type', 'text/html'),
                  ('Content-Length', str(len(response_body)))]
   start_response(status, response_headers)

   return [response_body]
