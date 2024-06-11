from app import create_app
from app import socketio

# Create an instance of the application using the create_app function
app = create_app()

if __name__ == "__main__":
    # Run the application with Socket.IO support
    # The following line is commented out, but can be used to run the app with Flask's built-in server
    # app.run(debug=True)
    
    # Run the app with Socket.IO server, which is better suited for handling real-time web applications
    socketio.run(app)