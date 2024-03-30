from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField, TextAreaField, SelectField, FloatField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from app.models import User, City, Category

class RegistrationForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired(), Length(min=2, max=100)])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(min=2, max=100)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email is already registered!')

class LoginForm(FlaskForm):
    email = StringField('email', validators=[DataRequired(), Email()])
    password = PasswordField('password', validators=[DataRequired(), Length(min=6)])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class UpdateAccountForm(FlaskForm):
    first_name = StringField('first_name', validators=[DataRequired(), Length(min=2, max=100)])
    last_name = StringField('last_name', validators=[DataRequired(), Length(min=2, max=100)])
    verification_number = StringField('verification_number', validators=[DataRequired(), Length(min=6, max=25)])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')

    def validate_verification_number(self, verification_number):
        if verification_number.data != current_user.verification_number:
            user = User.query.filter_by(verification_number=verification_number.data).first()
            if user:
                raise ValidationError('Verification number is already registered!')
            

class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    price = IntegerField('Price', validators=[DataRequired()])
    city = SelectField('City', choices=[(city.value) for city in City], validators=[DataRequired()])
    picture = FileField('Instrument Picture', validators=[FileAllowed(['jpg', 'png'])])
    category = SelectField('Category', choices=[(category.value) for category in Category], validators=[DataRequired()])
    submit = SubmitField('post')