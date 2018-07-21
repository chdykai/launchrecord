from flask import render_template
from launchrecord import app


@app.route('/')
def index():
    return render_template('index.html')


