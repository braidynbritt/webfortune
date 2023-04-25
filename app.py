from flask import (
    abort, Flask, jsonify, redirect, render_template, request,
    session, url_for
)

app = Flask(__name__)

@app.route('/')
def index():
    return 'hello world'

