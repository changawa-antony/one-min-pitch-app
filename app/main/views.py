from flask import Flask
from flask import render_template
from .forms import ReviewForm
from . import Blueprint
import app

# Views
@app.route('/')
def index():
    
    '''
    View root page function that returns the index page and its data
    '''

    # Getting popular movie
    title = "One min pitch"
    return render_template('index.html', title = title)

@app.route('/login')
def login():
    
    '''
    View root page function that returns the index page and its data
    '''

    # Getting popular movie
    title = "One min pitch"
    return render_template('login.html', title = title)

@app.route('/post')
def post():
    
    '''
    View root page function that returns the index page and its data
    '''

    # Getting popular movie
    title = "One min pitch"
    return render_template('post.html', title = title)

