"""Populates the database with a predefined list of drinks."""


from app import create_app  # Import the Flask application instance
from app import db  # Import the SQLAlchemy object
from models import Drink  # Import the Drink model

app = create_app()

# Sample entries to add
drinks_data = [
    {"name": "Coca-Cola", "description": "A classic cola drink."},
    {"name": "Pepsi", "description": "Another popular cola drink."},
    {"name": "Sprite", "description": "A refreshing lemon-lime soda."},
    {"name": "Fanta", "description": "A fruit-flavored soda available in various flavors."},
]

def add_drinks():
    """
    This function adds a predefined list of drinks to the database.
    Each drink is represented by a dictionary with 'name' and 'description' keys.
    Example of a drink entry: {"name": "Coca-Cola", "description": "A classic cola drink."}
    """
    # Push an application context
    with app.app_context():
        for drink in drinks_data:
            new_drink = Drink(name=drink["name"], description=drink["description"])
            db.session.add(new_drink)

        # Commit the session to save the new Drink objects to the database
        db.session.commit()


if __name__ == '__main__':
    add_drinks()
    print("Drinks added to the database.")
