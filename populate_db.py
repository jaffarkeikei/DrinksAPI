"""Populates the database with a predefined list of drinks."""


from app import create_app
from app import db
from models import Drink

app = create_app()

# Sample entries
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
    with app.app_context():
        for drink in drinks_data:
            new_drink = Drink(name=drink["name"], description=drink["description"])
            db.session.add(new_drink)

        db.session.commit()


if __name__ == '__main__':
    add_drinks()
    print("Drinks added to the database.")
