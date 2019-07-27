from flask import render_template, request, redirect, url_for, abort
from server import app, system
from system import System
from receipt import Receipt
from user import User
from item import Item

# @app.route('/', methods=["GET", "POST"])
# def login():



@app.route('/home', methods=["GET", "POST"])
def home():
    # bunch of redirects here depending on what the the user chooses to see or do
    if request.method == "POST":
        if "start" in request.form:
            return redirect(url_for('view', categories=system.getCategories()))
    return render_template('home/index.html')

@app.route('/<company>/<id>/receipt', methods=["GET", "POST"]) # accessed here through QR code
# name of '/receipt' can change later- possibly to a code system that we may
# implement
def save(company, id):
    # system.user_receipt('sample.json', 1)
    if request.method == "POST":
        if "save_receipt" in request.form:
            if request.form["save_receipt"] == True:
                saved = system.user_receipt('sample.json', 1) # hardcoded! returns boolean
                # do some error handling here for when the receipt does not belong
                # to the same user
    return redirect(url_for('view', categories=system.getCategories()))






#                 if saved == True:
#                     return redirect(url_for('success'))
#                 else:
#                     return redirect('fail')
# @app.route('/saved', methods=["GET", "POST"])
# def success():
#     string = system.receipts[-1].viewReceipt()
#     return render_template('success.html', string=string)
#
# @app.route('/unsaved', methods=["GET", "POST"])
# def fail():
#     return render_template('fail.html')
@app.route('/view', methods=["GET", "POST"])
def view(categories):
    # return stores based on category
    if request.method == "POST":
        for c in system.getCategories():
            if c in request.form:
                for u in system._user:
                    if u.id == 1:
                        company = u.retrieveCompany(c)
                else:
                    # render_template("home/main.html" company=company)
                    for u in system._user:
                        if u.id == 1:
                            company = u.retrieveCompany("all")
                            for name in company:
                                if name in request.form:
                                    return redirect(url_for('store', name=name))
    company = []
    for u in system._user:
        if u.id == 1:
            company = u.retrieveCompany("all")
            return render_template("home/main.html", categories=categories, company=company)



@app.route('/view/<name>', methods=["GET","POST"])
def store(name):
    # if request.method == "POST":
    receiptList =[]
    for u in system._user:
        if u._id == 1:
            receiptList = u.receiptStore(name)
    id = []
    date = []
    cost = []

    for r in receiptList:
        id.append(r._id)
        date.append(r._date)
        cost.append(r._calculateTotal)
    length = len(id)
    return render_template("home/company_receipt.html", id=id, date=date, cost=cost, length=length)
@app.route('/view/store/receipt', methods=["GET","POST"])
def receipt():
    if request.method == "POST":
        for u in system.user:
            if u.id == 1:
                for r in u._receipts:
                    if r._id == request.form["id"]:
                        receipt = r
                        return render_template("home/receipt.html", receipt=receipt)
        return redirect(url_for('store'))
