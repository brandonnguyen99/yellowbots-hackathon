# -*- coding: utf-8 -*-
from flask import Blueprint, render_template

blueprint = Blueprint('home', __name__)

@blueprint.route('/')
def index():
    return render_template('home/index.html')

@blueprint.route('/404')
def error():
    return render_template('404.html')

@blueprint.route('/company_receipt/<company>/<length>/<date>/<cost>/<id>')
def company_receipt(company, length, date, cost, id):
    
    return render_template('home/company_receipt.html', company = company, length = length, date = date, cost = cost, id = id);

@blueprint.route('/add_receipt')
def add_receipt():
    return render_template('home/add_receipt.html');

@blueprint.route('/main')
def main():
    return render_template('home/main.html');
