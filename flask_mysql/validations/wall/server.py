from flask import Flask
from flask_app.controllers import users
from flask_app.controllers import sent_msgs
from flask_app.controllers import rec_msgs
from flask_app import app

if __name__ == "__main__":
    app.run(debug=True)

