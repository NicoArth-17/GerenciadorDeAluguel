from __init__ import app
from flask import render_template, url_for, redirect

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/home')
def home():
    return render_template('home.html')