from flask import Flask, render_template, url_for,  session, redirect, flash
from flask_moment import Moment
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)

# hello.py - Example 3.4 - Using Flask-Bootstrap
Bootstrap = Bootstrap(app)

# Example 3.11 - Using Flask-Moment
Moment = Moment(app)

# Example 4.7 - modification for email field
class User_Info(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    email = StringField('What is your UofT email address?', validators=[DataRequired()])
    submit = SubmitField('Submit')

# Example 4.7 - Handling form submissions
@app.route('/', methods=['GET', 'POST'])
def index():
    form = User_Info()
    if form.validate_on_submit():
        old_name = session.get('name')
        old_email = session.get('email')

        # Flash messages for changes
        if old_name and old_name != form.name.data:
            flash('Looks like you have changed your name!')
        if old_email and old_email != form.email.data:
            flash('Looks like you have changed your email!')
        
        session['name'] = form.name.data
        session['email'] = form.email.data
        
        return redirect(url_for('index'))

    return render_template(
        'index.html',
        form=form,
        name=session.get('name'),
        email=session.get('email')
    )

# hello.py - Example 2.2 - Dynamic Routing
@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

# hello.py - Example 3.6 - Custom Error Pages
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

if __name__ == "__main__":
    app.run(debug=True)