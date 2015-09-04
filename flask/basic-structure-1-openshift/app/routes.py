import sys
from flask import Flask, render_template
from app import flaskapp

system = sys
print 'flask' in system.modules
# boolean

@flaskapp.route('/')
def hello_world():
    return '''
    Hello World!!!!
    <h1>Routes</h1>
    <p>GET: /</p>
    <p>GET: /dave</p>
    <p>GET: /user</p>
    <p>GET: /home</p>
    <p>GET: /about</p>
    '''

@flaskapp.route('/dave')
def myDave():
    return 'Hello World - From Dave'

@flaskapp.route('/home')
def home():
  return render_template('home.html')

@flaskapp.route('/about')
def about():
  return render_template('about.html')
