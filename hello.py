from flask import Flask
app = Flask(__name__)

# hello.py - Example 2.1 - Simple Route
@app.route('/')
def index():
    return '<h1>Hello, World!</h1>'

# hello.py - Example 2.2 - Dynamic Routing
@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, {}!</h1>'.format(name)