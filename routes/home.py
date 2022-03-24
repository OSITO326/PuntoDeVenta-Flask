from flask import (
    Blueprint, render_template, request, redirect, url_for, flash
)
from werkzeug.security import check_password_hash, generate_password_hash
from utils.db import db

home = Blueprint('home', __name__)


@home.route('/')
def welcome():
    return redirect(url_for('user.login'))
