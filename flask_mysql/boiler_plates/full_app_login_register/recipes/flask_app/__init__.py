from flask import Flask

from flask_app.models.user import User
from flask_app.models.recipe import Recipe

app = Flask(__name__)
app.secret_key = "Benny Bob wuz heer."