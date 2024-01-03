from flask import render_template
from main import app

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/<selectedNav>')
def selected(selectedNav):
    return render_template(f'{selectedNav}')