# Python + WSGI - Python for Web

1. Install WSGI into Apache,

    ref:

    * https://www.youtube.com/watch?v=E7HZyWAWe0E
    * https://www.youtube.com/watch?v=bRnm8f6Wavk
    * https://www.youtube.com/watch?v=iyXyxvs-544


2. Configure Apache config file,

    ```
    Loading Module Into Apache

    LoadModule wsgi_module modules/mod_wsgi.so

    <Directory /var/www/wsgi>
    ...
    Options ExecCGI
    AddHandler wsgi-script .py
    ...
    </Directory>

    <IfModule dir_module>
        DirectoryIndex ... index.py
    </IfModule>
    ```

3. Create the application function just as mod_wsgi expects the main function called to be named `application`,

    ```
    def application(environ, start_response):

        status = '200 OK'

        output = '<html><body>Hello World!</body></html>'

        response_headers = [('Content-type', 'text/html'),
        ('Content-Length', str(len(output)))]
        start_response(status, response_headers)

        return [output]
    ```

    or,

    ```
    def application(environ, start_response):
        status = '200 OK'
        output = 'Hello World!'

        response_headers = [('Content-type', 'text/plain'),
                            ('Content-Length', str(len(output)))]
        start_response(status, response_headers)

        return [output]
    ```


# MySQL for Python

    Ref:

    * https://pypi.python.org/pypi/MySQL-python/1.2.5
    * https://www.youtube.com/watch?v=ooIB8ZJattw
    * http://www.tutorialspoint.com/python/python_database_access.htm

# Python Template Engine

1. Install the module,

    `easy_install Jinja2`

    or

    `pip install Jinja2`

2. Basic API Usage

    ```
    >>> from jinja2 import Template
    >>> template = Template('Hello {{ name }}!')
    >>> template.render(name='John Doe')
    u'Hello John Doe!'
    ```

## Ref:

    * http://jinja.pocoo.org/

# WSGI + Flask

1. Create an index.py,

    ```
    import os
    import sys

    # mod_wsgi likely doesn't know about your virtualenv, and simply needs to be told
    # to use that rather than the default system environment.
    activate_this = os.path.dirname(__file__) + '/Scripts/activate_this.py'
    exec(open(activate_this).read(), dict(__file__ = activate_this))

    # Path to your directory that stores the app.
    #sys.path.append('C:/EasyPHP-DevServer/data/localweb/python-boilerplates/wsgi/flaskapp')
    sys.path.insert(0, os.path.dirname(__file__))

    from hello import app as application
    ```

    Then you can access the app via http://127.0.0.1/.../flaskapp/index.py/dave

    If you can access the apache config,

    ```
    <VirtualHost 127.0.0.1>
        ...
        <Directory "${path}/data/localweb">
            ...
        </Directory>
        WSGIScriptAlias / C:\...\flaskapp\index.py
    </VirtualHost>
    ```

    Now you can access the flask app from http://127.0.0.1/

## Ref:

    * http://blog.davidvassallo.me/2013/04/26/from-php-to-python-getting-started-with-mod_wsgi/
    * http://flask.pocoo.org/docs/0.10/deploying/mod_wsgi/
    * http://stackoverflow.com/questions/28144498/import-error-no-module-named-flask

# WSGI debugger

The cgitb module is for use with CGI scripts, not WSGI applications. Instead see https://code.google.com/p/modwsgi/wiki/DebuggingTechniques#Error_Catching_Middleware but don't use such things on production servers.

1. Install Paste for using it,

    `pip install paste`

2. Add this to the bottom of your .py,

    ```
    from paste.exceptions.errormiddleware import ErrorMiddleware
    application = ErrorMiddleware(application, debug=True)
    ```
