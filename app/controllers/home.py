# # -*- coding: utf-8 -*-
# from flask import Blueprint, render_template
#
# blueprint = Blueprint('home', __name__)
#
# @blueprint.route('/')
# def index():
#     return render_template('home/index.html')

from flask import render_template, request, redirect, url_for, abort
from server import app, system
from receipt import Receipt
from system import System
from user import User
from item import Item

@app.route('/home', methods=["GET", "POST"])
def home():
    # bunch of redirects here depending on what the the user chooses to see or do
    return render_template('home.html')

@app.route('/receipt', methods=["GET", "POST"]) # accessed here through QR code
# name of '/receipt' can change later- possibly to a code system that we may
# implement
def save():
    # system.user_receipt('sample.json', 1)
    if request.method == "POST":
        if "save_receipt" in request.form:
            if request.form["save_receipt"] == True:
                saved = system.user_receipt('sample.json', 1) # hardcoded! returns boolean
                # do some error handling here for when the receipt does not belong
                # to the same user
                if saved == True:
                    return redirect(url_for('success'))
                else:
                    return redirect('fail')
@app.route('/saved', methods=["GET", "POST"])
def success():
    string = system.receipts[-1].viewReceipt()
    return render_template('success.html', string=string)

@app.route('/unsaved', methods=["GET", "POST"])
def fail():
    return render_template('fail.html')
@app.route('/view', methods=["GET", "POST"])
def view():
