from . import bp as app
from flask import render_template
from flask_login import current_user

@app.route('/')
def home():
    return render_template('home.html', user=current_user)

@app.route('/about')
def about():
    return render_template('about.html')