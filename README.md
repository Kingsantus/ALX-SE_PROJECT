# ALX-SE_PROJECT
# Musical Instrument Rental Website

This project is a professional and formal website designed for the purpose of renting musical instruments. The website allows users to browse and rent a variety of musical instruments ranging from keyboards and synthesizers to guitars, drums, and more.

## Features

- **User Registration and Authentication**: Users can register for an account and log in securely to the website.
- **Browse Instruments**: Users can browse through a wide range of musical instruments available for rent, categorized by type and location.
- **Rent Instruments**: Users can select the desired instrument and initiate the rental process securely through the website.
- **User Reviews**: Users can read and leave reviews for instruments they have rented, providing valuable feedback for other users.
- **Responsive Design**: The website is designed to be responsive, ensuring optimal viewing and interaction across various devices and screen sizes.

## Technologies Used

- **Flask**: The website is built using the Flask web framework, providing a robust and flexible foundation for web development.
- **SQLAlchemy**: SQLAlchemy is used as the ORM (Object-Relational Mapping) tool for interacting with the database, allowing for efficient management of data.
- **SQLite**: SQLite is used as the database management system for storing user data, instrument information, and rental agreements.
- **HTML/CSS/JavaScript**: Standard web technologies are utilized for designing and styling the user interface and implementing interactive features.
- **Bootstrap**: Bootstrap framework is employed for front-end development, ensuring consistency and responsiveness in design.
- **Python**: Python programming language is used for backend logic and server-side scripting.

## Setup Instructions

1. **Clone the Repository**: Clone this repository to your local machine using the following command:

git clone https://github.com/Kingsantus/ALX-SE_PROJECT.git

2. **Install Dependencies**: Navigate to the project directory and install the required dependencies using pip:

cd musical-instrument-rental
pip install -r requirements.txt


3. **Database Setup**: Initialize the SQLite database by running the following commands:

flask db init
flask db migrate
flask db upgrade


4. **Run the Application**: Start the Flask development server by running:

flask run


5. **Access the Website**: Open your web browser and navigate to `http://localhost:5000` to access the website.

## Contributors

- [Asogwa Kingsantus N](https://github.com/Kingsantus)
- [#](https://github.com/#)

## License

This project is licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute the code for your own projects.

 
