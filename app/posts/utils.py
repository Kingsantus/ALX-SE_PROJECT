import os, secrets
from PIL import Image
from flask import current_app

def post_picture(form_picture):
    """
    Save a post picture uploaded by the user.
    Generates a random filename, resizes the image, and saves it to the static folder.

    Args:
        form_picture: The uploaded picture file.

    Returns:
        The filename of the saved picture.
    """
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path, 'static\\images\\post_pic', picture_fn)
    output_size = (400, 400)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    return picture_fn
