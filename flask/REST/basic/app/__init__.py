from flask import Flask

# Initialize the Flask application
app = Flask(__name__)

from app import routes
