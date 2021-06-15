from app import app
from flask import render_template

# Views
@app.route('/')
def index():
    
    '''
    View root page function that returns the index page and its data
    '''

    # Getting popular movie
    title = "One min pitch"
    return render_template('index.html', title = title)

