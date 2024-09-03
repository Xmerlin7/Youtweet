#!/usr/bin/env python3
"""_summary_: all project Imports will be added here
"""
from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect
from youtweet.validator import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
#! token = secrets.token_hex(16)
app.config['SECRET_KEY'] = '53665e59e6730130595ea71c41e3eecd'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
from youtweet.models import User, Post

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

#? GET:  Typically used to display the registration form to the user.
#? POST: Used to submit the registration form data to the server.
@app.route('/about')
def about():
    """_summary_

    Returns:
        _type_: _description_
    """
    return render_template('about.html', title='About')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Registration successful for {form.username.data}', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@example.com' and form.password.data == 'password123':
            flash('Login successful!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login failed! Please check your email and password.', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)