from flask import Flask, render_template
from flask_restful import Resource, Api

from app import app

api = Api(app)

TODOS = {
    'todo1': {'task': 'build an API'},
    'todo2': {'task': '?????'},
    'todo3': {'task': 'profit!'},
}

class HelloWorld(Resource):

    def get(self):
        return {'hello': 'world', 'GET': '/user/<string:todo_id>', 'PUT': '/user/<string:todo_id>', 'DELETE': '/user/<string:todo_id>','GET': '/users', 'POST': '/users'}

class TodoSimple(Resource):

    def get(self, todo_id):
        return {'id': todo_id, 'method': 'GET'}

    def put(self, todo_id):
        return {'id': todo_id, 'method': 'PUT'}

    def delete(self, todo_id):
        return {'id': todo_id, 'method': 'DELETE'}

class TodoList(Resource):

    def get(self):
        return TODOS

    def post(self):
        todo_id = int(max(TODOS.keys()).lstrip('todo')) + 1
        todo_id = 'todo%i' % todo_id
        TODOS[todo_id] = {'task': todo_id, 'method': 'POST'}
        return TODOS[todo_id], 201 # CREATED 201

        """
        CREATED 201
        Following a POST command, this indicates success, but the textual part of the response line indicates the URI by which the newly created document should be known.
        """

api.add_resource(HelloWorld, '/')
api.add_resource(TodoList, '/users')
api.add_resource(TodoSimple, '/user/<string:todo_id>')
