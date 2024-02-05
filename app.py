"""
This is the main script for the Flask application.
It creates the Flask app, initializes the database, registers the routes, and runs the app.
"""



from flask import Flask
from extensions import db
from routes import routes

def create_app():
    """
    This function creates the Flask app, initializes the database, registers the routes, and runs the app.
    """
    flask_app = Flask(__name__)
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
    db.init_app(flask_app)
    flask_app.register_blueprint(routes)
    return flask_app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
    print("The Flask application is running successfully.")
