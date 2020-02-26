from flask import Flask, Blueprint

home_routes = Blueprint("home_routes", __name__)

@home_routes.route('/')
def index():
    return "Hello"

@home_routes.route('/about')
def about():
    return "about me"
        
