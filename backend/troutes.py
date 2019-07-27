from server import app, valid_time, login_manager
from flask import request, render_template, url_for, redirect, abort\
from flask_login import LoginManager, login_user, current_user, login_required, logout_user
from system import System
from user import User

import csv
from datetime import datetime

@app.route('/', methods=['GET', 'POST'])
def login():
    failed = 0
    if request.method == 'POST':
		#Authentication
		emailID = request.form['emailid']
		password = request.form['password']
        user = system.login(id, password)
        if user != False:
            login_user(user)
            userView = current_user
            # return redirect(url_for(...))
        else:
            failed = 1
        return render_template('login.html', failed=failed)

    return render_template('login.html', failed=failed)

@login_manager.user_loader
def load_user(id):
    return system.validateID(id)

@app.route("/logout")
@login_required
def logout():
	logout_user()
	return redirect(url_for('login'))

