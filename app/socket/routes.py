from flask_socketio import emit
from app import socketio, db
from flask_login import current_user
from datetime import datetime
from .utils import get_user_image_file
from app.models import Message

# SocketIO event handler for new messages
@socketio.on('send_message')
def handle_message(data):
    """
    Handle incoming messages sent by users in real-time.

    Args:
        data: A dictionary containing message data, including content, chat_id, etc.
    """
    # Extract message data from the incoming data dictionary
    content = data['content']
    chat_id = data['chat_id']
    # Get the ID of the current user sending the message
    user_id = current_user.id
    # Get the current timestamp
    timestamp = datetime.utcnow()
    # Get the filename of the user's image file
    user_image_file = get_user_image_file(user_id)
    # Format the timestamp as a string
    timestamp_str = timestamp.strftime('%H:%M')

    # Save the message to the database
    message = Message(content=content, chat_id=chat_id, user_id=user_id, timestamp=timestamp)
    db.session.add(message)
    db.session.commit()
    # Emit a 'receive_message' event to all clients
    emit('receive_message', {'content': content, 'chat_id': chat_id, 'user_image_file': user_image_file, 'timestamp': timestamp_str}, broadcast=True)