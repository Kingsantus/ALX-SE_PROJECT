
from flask import url_for, current_app
import secrets, os
from PIL import Image
from app import  mail
from flask_mail import Message

def save_picture(form_picture):
    """
    Save a profile picture uploaded by the user.
    Generates a random filename, resizes the image, and saves it to the static folder.

    Args:
        form_picture: The uploaded picture file.

    Returns:
        The filename of the saved picture.
    """
    # Generate a random hexadecimal string for the new filename
    random_hex = secrets.token_hex(8)
    # Extract the file extension from the original filename
    _, f_ext = os.path.splitext(form_picture.filename)
     # Combine the random hex string and file extension to form the new filename
    picture_fn = random_hex + f_ext
    # Define the path to save the picture
    picture_path = os.path.join(current_app.root_path, 'static\\images\\profile_pic', picture_fn)
    # Resize the image to 125x125 pixels
    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    # Save the resized image to the defined path
    i.save(picture_path)
    # Return the filename of the saved picture
    return picture_fn


def send_reset_email(user):
    """
    Send a password reset email to the user.
    Generates a reset token and sends an email with a link to reset the password.

    Args:
        user: The user to send the reset email to.
    """
     # Generate a reset token for the user
    token = user.get_reset_token()
      # Create an email message
    msg = Message('Password Reset Request', sender='noreply@demo.com', recipients=[user.email])
    # Define the body of the email with a link to reset the password
    msg.body = f"""To reset your password, visit the following link:
    {url_for('reset_token', token=token, _external=True)}
    If you did not make this request. Please ignore this email and no changes will be made.
    """
    # Send the email
    mail.send(msg)
