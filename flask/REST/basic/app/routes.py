from flask import Flask, jsonify, render_template
from app import app

@app.route('/')
@app.route('/index')
def hello_world():
    return '''
    Hello World!!!!
    <h1>Routes</h1>
    <p>GET: /</p>
    <p>GET: /dave</p>
    <p>GET: /home</p>
    <p>GET: /about</p>
    <p>GET: /json</p>
    <p>GET: /user</p>
    <p>POST: /user</p>
    <p>GET: /user/<user_id></p>
    <p>PUT: /user/<user_id></p>
    <p>DELETE: /user/<user_id></p>
    '''

# This route will return a list in JSON format
@app.route('/json')
def json():

    # This is a dummy list, 2 nested arrays containing some
    # params and values
    list = [
        {'param': 'foo', 'val': 2},
        {'param': 'bar', 'val': 10}
    ]

    # jsonify will do for us all the work, returning the
    # previous data structure in JSON
    return jsonify(results=list)

@app.route('/dave')
def myDave():
    return 'Hello World - From Dave'

@app.route('/home')
def home():
  return render_template('home.html')

@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/user', methods = ['POST'])
def postUser():
  return 'posted user'

@app.route('/user/<user_id>', methods = ['GET'])
def getUser(user_id):
  return 'get an user. user id: ' + user_id

@app.route('/user/<user_id>', methods = ['PUT'])
def putUser(user_id):
  return 'put user. user id: ' + user_id

@app.route('/user/<user_id>', methods = ['DELETE'])
def deleteUser(user_id):
  return 'deleted user. user id: ' + user_id

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
