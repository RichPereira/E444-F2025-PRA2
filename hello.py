from flask import Flask, render_template
from datetime import datetime
from flask_moment import Moment
from flask_bootstrap import Bootstrap
app = Flask(__name__)

# hello.py - Example 3.4 - Using Flask-Bootstrap
Bootstrap = Bootstrap(app)

# Example 3.11 - Using Flask-Moment
Moment = Moment(app)

# hello.py - Example 2.1 - Simple Route
@app.route('/')
def index():
    return render_template('index.html')

# hello.py - Example 2.2 - Dynamic Routing
@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name, current_time=datetime.utcnow())

# hello.py - Example 3.6 - Custom Error Pages
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

