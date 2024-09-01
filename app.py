#!/usr/bin/env python3
"""_summary_: all project Imports will be added here
"""
from flask import Flask, render_template, url_for, flash, redirect
from validator import RegistrationForm, LoginForm
app = Flask(__name__)
#! token = secrets.token_hex(16)
app.config['SECRET_KEY'] = '53665e59e6730130595ea71c41e3eecd'
posts = [
    {
        'author': 'John Doe',
        'title': 'Blog Post 1',
        'content': 'First post on YouTweet',
        'date_posted': 'April 20, 2020'
    },
    {
        'author': 'Jane Smith',
        'title': 'Blog Post 2',
        'content': 'Second post on YouTweet',
        'date_posted': 'April 20, 2020'
    }]
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
    return render_template('about.html', title='About')
@app.route('/contact')
def contact():
    return "<h1>Welcome to the Contact Page!</h1>"

if __name__ == '__main__':
    app.run(debug=True)