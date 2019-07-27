from flask import Flask
from init import receiptSystem

app = Flask(__name__)
app.config['SECRET_KEY'] = 'very-secret-123'  # Used to add entropy

system = receiptSystem()
system.add_users()
