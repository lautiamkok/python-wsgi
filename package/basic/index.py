import os
import sys

root = os.path.dirname(__file__)
sys.path.append(root + "/packages")

# IMPORTS PACKAGES
import hello

# This is our application object. It could have any name,
# except when using mod_wsgi where it must be "application"
def application(environ, start_response):

    results = []

    results.append(hello.hello())

    helloWorld = hello.HelloWorld()
    results.append(helloWorld.sayHello())

    output = "<br/>".join(results)

    # build the response body possibly using the environ dictionary
    response_body = output

    # HTTP response code and message
    status = '200 OK'

    # These are HTTP headers expected by the client.
    # They must be wrapped as a list of tupled pairs:
    # [(Header name, Header value)].
    response_headers = [('Content-Type', 'text/html'),
                       ('Content-Length', str(len(response_body)))]

    # Send them to the server using the supplied function
    start_response(status, response_headers)

    # Return the response body.
    # Notice it is wrapped in a list although it could be any iterable.
    return [response_body]
