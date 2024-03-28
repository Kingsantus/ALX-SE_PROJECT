from flask import render_template, url_for, flash, redirect
from app import app, db, bcrypt
from app.forms import RegistrationForm, LoginForm
from flask_login import login_user, current_user, logout_user
from app.models import User, Post, Review, Agreement

posts = [
    {
        'author': "Williams Joe",
        'title': "Washburn Elegante S24S Bella Tono Studio",
        'category': "Acostic",
        'price': 5000,
        'location': "Enugu, Nigeria",
        'discount': 0.05,
        'discription': "Good Sound and electrical",
        'date_posted': "March 27, 2024"
    },
    {
        'author': "Kelvin Finder",
        'title': "Medeli Electronics AKX10 Arranger Pro Digital Workstation",
        'category': "Keyboard",
        'price': 10000,
        'location': "Anambra, Nigeria",
        'discount': 0.03,
        'discription': "Good Sound and electrical",
        'date_posted': "March 25, 2024"
    }
]

@app.route("/")
@app.route("/home")
@app.route("/index")
def home():
    return render_template('index.html', posts=posts)


@app.route("/signup", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(first_name=form.first_name.data, last_name=form.last_name.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f"Your account has been created! You are now able to log in", 'success')
        return redirect(url_for('login'))
    return render_template('signup.html', form=form, title='Signup')

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', form=form, title='Login')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))
