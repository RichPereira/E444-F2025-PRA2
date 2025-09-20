from flask import Flask, render_template
from datetime import datetime
from flask_bootstrap import Bootstrap
app = Flask(__name__)

# hello.py - Example 2.1 - Simple Route
@app.route('/')
def index():
    return render_template('index.html')

# hello.py - Example 2.2 - Dynamic Routing
@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name, timestamp=datetime.now())

# hello.py - Example 2.3 - Using Flask-Bootstrap
Bootstrap = Bootstrap(app)