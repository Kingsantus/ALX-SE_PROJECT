from app.models import User

def get_user_image_file(user_id):
    """
    Retrieve the image file associated with a user.

    Args:
        user_id: The ID of the user whose image file is to be retrieved.

    Returns:
        The filename of the user's image file if the user exists, otherwise None.
    """
    # Retrieve the user with the specified user_id from the database
    user = User.query.get(user_id)
    # If the user exists, return the filename of the user's image file
    if user:
        return user.image_file
    # If the user does not exist, return None
    return None 

