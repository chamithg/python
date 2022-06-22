from flask import Flask

from flask_app.models.user import User
from flask_app.models.sent_msg import Sent_msg
from flask_app.models.rec_msg import Rec_msg
app = Flask(__name__)
app.secret_key = "Benny Bob wuz heer."