from flask import Flask
# from routes.home import home
from routes.user import user
# from routes.menu import menu
from flask_sqlalchemy import SQLAlchemy
from config import DATABSE_CONNECTION_URI

app = Flask(__name__)

app.secret_key = 'secret key'
app.config['SQLALCHEMY_DATABASE_URI'] = DATABSE_CONNECTION_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

SQLAlchemy(app)

app.register_blueprint(user)
