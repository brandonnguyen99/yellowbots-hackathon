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

# @app.route('/', methods=["GET", "POST"])
# def login():



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
    # return stores based on category
    if request.form == "POST":
        if "category" in request.form:
            categoryComp = []
            category = request.form["category"]
            for u in system._user:
                if u.id == 1:
                    categoryComp = u.retrieveCompany(category)
            if not categoryComp:
                # render template for empty
                False
            else:
                render_template("main.html" categoryComp=categoryComp)
    return render_template("main.html")


@app.route('/view/store', methods=["GET","POST"])
def store():
    if request.form == "POST":
        if "store" in request.form:
            store_receipts = []
            store = request.form["store"]
            for u in system._user:
                if u._id == 1:
                    store_receipts = u.receiptStore()
            if not store_receipts:
                False
                #error return render_template
            else:
                return render_template("receipts.html", store_receipts=store_receipts)
        if "id" in request.form:
            return redirect(url_for('receipt'))
@app.route('/view/store/receipt', methods=["GET","POST"])
def receipt():
    if request.form == "POST":
        for u in system.user:
            if u.id == 1:
                for r in u._receipts:
                    if r._id == request.form["id"]:
                        receipt = r
                        return render_template("receipts_show.html", receipt=receipt)
        return redirect(url_for('store'))
