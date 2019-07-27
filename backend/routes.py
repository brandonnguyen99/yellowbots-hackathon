from flask import render_template, request, redirect, url_for, abort
from server import app, system
from flask_login import LoginManager, login_user, current_user, login_required, logout_user
from receipt import Receipt
from system import System
from user import User
from item import Item

@app.route('/', methods=["GET", "POST"])
def home():
    return render_template('home.html')

@app.route('/receipt', methods=["GET", "POST"])
def save():
    
