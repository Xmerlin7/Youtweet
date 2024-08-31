#!/usr/bin/env python3
"""_summary_: all project Imports will be added here
"""
from  flask import Flask, render_template
app = Flask(__name__)
posts = "helook"
@app.route('/')
@app.route('/home')
def home():
    """_summary_:

    Returns:
        _type_: String type
    """
    return render_template('home.html', posts=posts)
@app.route('/about')
def about():
    """_summary_

    Returns:
        _type_: _description_
    """
    return "<h1>Welcome to the About Page!</h1>"
@app.route('/contact')
def contact():
    return "<h1>Welcome to the Contact Page!</h1>"

if __name__ == '__main__':
    app.run(debug=True)