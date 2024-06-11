from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from app.models import User, City
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user

class RegistrationForm(FlaskForm):
    """
    Form for user registration. Contains fields for first name, last name,
    email, phone number, password, and password confirmation.
    """
    first_name = StringField('First Name', validators=[DataRequired(), Length(min=2, max=100)])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(min=2, max=100)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone_number = StringField('Phone Number', validators=[DataRequired(), Length(min=11, max=15)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_email(self, email):
        """
        Custom validator to check if the email is already registered.
        """
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email is already registered!')

class LoginForm(FlaskForm):
    """
    Form for user login. Contains fields for email and password, and a
    remember me checkbox.
    """
    email = StringField('email', validators=[DataRequired(), Email()])
    password = PasswordField('password', validators=[DataRequired(), Length(min=6)])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class UpdateAccountForm(FlaskForm):
    """
    Form for updating account details. Contains fields for first name,
    last name, city, verification number, and profile picture.
    """
    first_name = StringField('First Name', validators=[DataRequired(), Length(min=2, max=100)])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(min=2, max=100)])
    city = SelectField('City', choices=[(city.value) for city in City], validators=[DataRequired()])
    verification_number = StringField('Verification Number', validators=[DataRequired(), Length(min=6, max=25)])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')

    def validate_verification_number(self, verification_number):
        """
        Custom validator to check if the verification number is correct
        and unique.
        """
        if verification_number.data != current_user.verification_number:
            user = User.query.filter_by(verification_number=verification_number.data).first()
            if user:
                raise ValidationError('Verification number is already registered!')

class RequestResetForm(FlaskForm):
    """
    Form to request a password reset. Contains a field for email.
    """
    email = StringField('email', validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')

    def validate_email(self, email):
        """
        Custom validator to check if the email is registered.
        """
        user = User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError('There is no account with the email, register first!')
        
class ResetPasswordForm(FlaskForm):
    """
    Form to reset the password. Contains fields for new password and
    password confirmation.
    """
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Reset Password')