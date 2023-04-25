import subprocess
import sys
from flask import (
    abort, Flask, jsonify, redirect, render_template, request,
    session, url_for
)

app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(e):
    return redirect(url_for('fortune'))

@app.route('/')
def index():
    return redirect(url_for('fortune'))

@app.route('/fortune/')
def fortune():
    output = subprocess.run(['fortune'], stdout=subprocess.PIPE)
    return f'<pre>{output.stdout.decode()}</pre>'
    
@app.route('/cowsay/<message>/')
def cowsay(message):
    output = subprocess.run(['cowsay', message], stdout=subprocess.PIPE)
    return f'<pre>{output.stdout.decode()}</pre>'

@app.route('/cowfortune/')
def cowfortune():
    fortune = subprocess.run(['fortune'], stdout=subprocess.PIPE)
    output = subprocess.run(['cowsay', fortune.stdout.decode()], stdout=subprocess.PIPE)
    return f'<pre>{output.stdout.decode()}</pre>'
