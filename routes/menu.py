from flask import (
    Blueprint, render_template, request, redirect, url_for, flash
)
from models.menu import Menu
from utils.db import db

# menu = Blueprint('menu', __name__)
menu = Blueprint('menu', __name__, url_prefix='/menu')


@menu.route('/')
def index():
    # return 'index'
    return redirect(url_for('menu.register_plate'))


@menu.route('/show_plates')
def show_plates():
    menu = Menu.query.all()
    return render_template('/menu/show.html', menu=menu)


@menu.route('/register_plate')
def register_plate():
    return render_template('menu/register.html')


@menu.route('/add_plate', methods=['POST'])
def add_plate():
    name = request.form['name']
    price = request.form['price']
    description = request.form['description']
    new_plate = Menu(name, price, description)
    db.session.add(new_plate)
    db.session.commit()
    # flash('Plate added successfully!')
    flash('Plate added successfully!')
    return redirect(url_for('menu.show_plates'))


@menu.route('/update_plate/<id>', methods=['GET', 'POST'])
def update_plate(id):
    update_plate = Menu.query.get(id)
    if request.method == 'POST':
        update_plate.name = request.form['name']
        update_plate.price = request.form['price']
        update_plate.description = request.form['description']
        db.session.commit()
        flash('Plate updated successfully!')
        return redirect(url_for('menu.show_plates'))

    return render_template('menu/update.html', plate=update_plate)


@menu.route('/delete_plate/<id>')
def delete_plate(id):
    delete_plate = Menu.query.get(id)
    db.session.delete(delete_plate)
    db.session.commit()
    flash('Plate deleted successfully!')
    return redirect(url_for('menu.show_plates'))


@menu.route('/about')
def about():
    return render_template('about.html')
