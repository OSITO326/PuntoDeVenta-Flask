import functools
from flask import (
    Blueprint, render_template, request, redirect, url_for, flash, session
)
from werkzeug.security import check_password_hash, generate_password_hash
from models.user import User
from utils.db import db


user = Blueprint('user', __name__, url_prefix='/auth')
# user = Blueprint('user', __name__)


@user.route('/')
def index():
    return redirect(url_for('user.login'))
    # return 'hola'


@user.route('/login')
def login():
    return render_template('auth/singin.html')


# @user.route('/login', methods=['GET', 'POST'])
# def login():
    # if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        # username = request.form['username']
        # password = request.form['password']
        # passhash = generate_password_hash(password)
        # user = User.query.filter_by(username=username).first()
        # check_pass = check_password_hash(user.password, password)
        # if passhash == check_pass:
            # flash('Please check your login details and try again.')
            # return redirect(url_for('home.go_home'))
    # if request.method == 'POST':
        # username = request.form['username']
        # password = request.form['password']
        # passhash = generate_password_hash(password)
        # user = User.query.filter_by(username=username).first()
        # pass_db = user.password
        # print(pass_db)
        # if password == passhash:
    # return render_template('auth/singin.html')
 # return redirect(url_for('user.login'))

# @user.route('/login', methods=['GET', 'POST'])
# def login():
    # if request.method == 'POST':
        # # username = request.form['username']
        # # check_user = User.query.filter_by(username=username).first()
        # # return render_template(url_for())
        # return render_template('auth/login.html')
    # else:
        # return render_template('auth/login.html')


@user.route('/register_user')
def register_user():
    return render_template('auth/register.html')


@user.route('/add_user', methods=['POST'])
def add_user():
    if request.method == 'POST':
        name = request.form['name']
        lastname = request.form['lastname']
        email = request.form['email']
        phone = request.form['phone']
        username = request.form['username']
        password = request.form['password']
        new_user = User(name, lastname, email, phone, username, generate_password_hash(password))
        db.session.add(new_user)
        db.session.commit()
        flash('User added successfully!')
        return redirect(url_for('user.login'))
    return 'error'


@user.route('/show_users', methods=['GET', 'POST'])
def show_users():
    user = User.query.all()
    if request.method == 'POST':
        return render_template('/auth/show.html', users=user)
        if request.method == 'GET':
            return render_template('/auth/show.html', users=user)
    return render_template('/auth/show.html', users=user)


@user.route('/update_user/<id>', methods=['GET', 'POST'])
def update_user(id):
    update_user = User.query.get(id)
    if request.method == 'POST':
        update_user.name = request.form['name']
        update_user.lastname = request.form['lastname']
        update_user.email = request.form['email']
        update_user.phone = request.form['phone']
        update_user.username = request.form['username']
        # update_user.password = request.form['password']
        db.session.commit()
        flash('User updated successfully!')
        return redirect(url_for('user.show_users'))
    return render_template('auth/update.html', user=update_user)


@user.route('/delete_user/<id>')
def delete_user(id):
    user_delete = User.query.get(id)
    db.session.delete(user_delete)
    db.session.commit()
    flash('User deleted successfully!')
    return redirect(url_for('user.login'))


@user.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home.welcome'))
