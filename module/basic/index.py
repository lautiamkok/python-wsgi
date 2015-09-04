import os
import sys

root = os.path.dirname(__file__)
sys.path.append(root + "/modules")
sys.path.append(root + "/modules/User")
sys.path.append(root + "/modules/Article")

# IMPORTS MODULES
import hello
import HelloWorld
import moduletest
import Users
import Articles

from moduletest import printhello
from hello import hello
from HelloWorld import HelloWorld
from Users import Users
from Articles import Articles

# This is our application object. It could have any name,
# except when using mod_wsgi where it must be "application"
def application(environ, start_response):

    results = []

    results.append(str(moduletest.ageofqueen))
    results.append(printhello())
    results.append(hello())

    helloWorld = HelloWorld()
    results.append(helloWorld.sayHello())

    user = Users()
    results.append(user.sayHello())

    article = Articles()
    results.append(article.sayHello())

    output = "<br/>".join(results)

    print output

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
