from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'c3f098f24c976404335b22ae39d67b92'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///rent.db'

db = SQLAlchemy(app)

from models import User, Post, Rating, Review, Agreement

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
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created for {form.email.data}!", 'success')
        return redirect(url_for('home'))
    return render_template('signup.html', form=form, title='Signup')

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'fin@gmail.com' and form.password.data == 'fin123':
            flash("You have been logged in!", 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', form=form, title='Login')


if __name__ == "__main__":
    app.run(debug=True)