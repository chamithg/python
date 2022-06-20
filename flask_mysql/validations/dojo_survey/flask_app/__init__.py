from flask import Flask
# import the class from friend.py
from flask_app.models.dojo import Dojo
app = Flask(__name__)
app.secret_key = "Benny Bob wuz heer."