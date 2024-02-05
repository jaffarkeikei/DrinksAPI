"""
This script defines the routes for the Flask application.

It includes routes for the home page, getting all drinks, adding a drink, getting a specific drink, and updating a drink.
"""


from flask import Blueprint, request, redirect, url_for, render_template
from sqlalchemy.exc import IntegrityError
from models import Drink
from extensions import db


routes = Blueprint('routes', __name__)


@routes.route('/')
def index():
    """
    Home page of the application.

    It returns a simple greeting message.
    """
    return 'Hello!'

@routes.route('/drinks')
def get_drinks():
    """
    Get all the drinks from the database.

    It returns a JSON object with the name and description of each drink.
    """
    drinks = Drink.query.all()
    drinks_data = [{"name": drink.name, "description": drink.description} for drink in drinks]
    return {"drinks": drinks_data}

@routes.route('/add_drink', methods=['GET'])
def show_add_drink_form():
    """
    Display the form for adding a new drink.

    It returns the HTML template for the form.
    """
    return render_template('crud.html')

@routes.route('/add_drink', methods=['POST'])
def add_drink():
    """
    Add a new drink to the database.

    It takes the name and description of the drink from the form data.
    If a drink with the same name already exists, it returns an error message.
    """
    name = request.form['name']
    description = request.form['description']
    new_drink = Drink(name=name, description=description)
    try:
        db.session.add(new_drink)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return "A drink with this name already exists.", 400
    return redirect(url_for('routes.show_add_drink_form'))

@routes.route('/drinks/<int:drink_id>', methods=['GET'])
def get_drink(drink_id):
    """
    Get a specific drink from the database.

    It takes the id of the drink as a parameter and returns a JSON object with the name and description of the drink.

    If the drink with the given id does not exist, it returns a 404 error.
    """
    drink = Drink.query.get_or_404(drink_id)
    return {"name": drink.name, "description": drink.description}

@routes.route('/drinks/<int:drink_id>', methods=['PUT'])
def update_drink(drink_id):
    """
    Update a specific drink in the database.

    It takes the id of the drink as a parameter and the new name and description of the drink from the form data.

    If the drink with the given id does not exist, it returns a 404 error.
    """
    drink = Drink.query.get_or_404(drink_id)
    drink.name = request.form['name']
    drink.description = request.form['description']
    db.session.commit()
    return {"message": "Drink updated successfully"}

@routes.route('/drinks/<int:drink_id>', methods=['DELETE'])
def delete_drink(drink_id):
    """
    Delete a specific drink from the database.

    It takes the id of the drink as a parameter.
    If the drink with the given id does not exist, it returns a 404 error.
    """
    drink = Drink.query.get_or_404(drink_id)
    db.session.delete(drink)
    db.session.commit()
    return {"message": "Drink deleted successfully"}
