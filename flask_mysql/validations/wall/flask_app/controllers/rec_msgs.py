from flask_app import app
from flask import render_template,request,redirect,session
from flask_app.models.rec_msg import Rec_msg
from flask import flash



@app.route("/delete/<int:msg_id>")
def delete_msg(msg_id):
    data ={"msg_id":msg_id }
    Rec_msg.delete(data)
    return redirect("/output")