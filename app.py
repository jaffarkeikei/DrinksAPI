"""
This section of the app.py file is dedicated to initializing the Flask application and setting up routes for the web service. It includes the creation of the Flask app, configuration of the database URI, initialization of the database with the Flask app, and definition of routes for the homepage and fetching drinks from the database.

The Flask application is configured to connect to a SQLite database named 'data.db'. The database is initialized with the Flask app using the `db.init_app(app)` method. Two routes are defined: the homepage route ('/') which returns a simple greeting, and the '/drinks' route which fetches all drinks from the database and returns them in a JSON format.

Example usage:
- Accessing the homepage by navigating to 'http://localhost:5000/' will display 'Hello!'.
- Accessing the drinks list by navigating to 'http://localhost:5000/drinks' will display a JSON object containing all drinks in the database.
"""


from flask import Flask
from extensions import db
from models import Drink


def create_app():
    """
    Initializes the Flask application with necessary configurations and database setup.
    
    This function creates a Flask application instance, configures it to use a SQLite database, initializes the database with the application, and defines routes for the application. It returns the configured Flask application instance.
    
    Returns:
        app: The Flask application instance configured with routes and database.
    
    Example:
        Creating an app instance and running it:
        
        app = create_app()
        app.run(debug=True)
        
        This will start a Flask web server running in debug mode, with routes defined for the homepage and fetching drinks.
    """
    flask_app = Flask(__name__)
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

    db.init_app(flask_app)

    # Define routes
    @flask_app.route('/')
    def index():
        return 'Hello!'

    @flask_app.route('/drinks')
    def get_drinks():
        drinks = Drink.query.all()
        drinks_data = [{"name": drink.name, "description": drink.description} for drink in drinks]
        return {"drinks": drinks_data}

    return flask_app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
