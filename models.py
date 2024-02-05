"""
This module defines the Drink model for the database schema, including its fields and representation.
The Drink model includes fields for id, name, and description, and provides a string representation of itself.
Example:
    A Drink instance with name='Coca-Cola' and description='A classic cola drink.' will be represented as:
    <Drink Coca-Cola>
"""


from extensions import db

class Drink(db.Model):
    """
    Defines the Drink model's database fields and provides a string representation.

    Fields:
        id (Integer): The primary key.
        name (String): The name of the drink, must be unique and not nullable.
        description (String): The description of the drink, must be unique and not nullable.

    Example:
        Creating a Drink instance with name='Lemonade' and description='A sweetened lemon-flavored beverage' will be represented as:
        <Drink Lemonade>
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(120), unique=True, nullable=False)

    @classmethod
    def __repr__(self):
        """
        Returns a string representation of the Drink instance.

        This method overrides the default representation method to provide a more descriptive string representation of Drink instances. It includes the name of the drink.

        Example:
            For a Drink instance with name='Coca-Cola', the representation will be:
            <Drink Coca-Cola>
        """
        return f'<Drink {self.name}>'

    @classmethod
    def find_by_name(cls, name):
        """
        This class method searches for a drink by its name and returns the drink instance if found.

        Args:
            name (String): The name of the drink to search for.

        Returns:
            Drink instance if found, otherwise None.

        Example:
            Let's say we have a Drink instance with name='Coca-Cola' in the database.
            Calling Drink.find_by_name('Coca-Cola') would return the <Drink Coca-Cola> instance.
        """
        return cls.query.filter_by(name=name).first()
