from flask import Flask
from init import receiptSystem
from flask_login import LoginManager, login_manager, login_user, current_user, login_required, logout_user

app = Flask(__name__)
app.secret_key = 'very-secret-123'  # Used to add entropy

system = receiptSystem()
system._add_users()
