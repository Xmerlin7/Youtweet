from flask import render_template, url_for, flash, redirect
from youtweet.forms import RegistrationForm, LoginForm
from youtweet.models import User
from youtweet import app, db, bcrypt

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
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Your account has been created! You are now able to login', 'success')
        return redirect(url_for('login'))
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
