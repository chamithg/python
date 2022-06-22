from flask_app import app
from flask import render_template,request,redirect,session
from flask_app.models.rec_msg import Rec_msg
from flask_app.models.sent_msg import Sent_msg
from flask import flash


@app.route("/send_msg/<int:id>", methods =["POST"])
def send_msg(id):
    data ={"receiver_id":id, "sender":request.form["sender"],"sent_msg":request.form["msg_content"] }
    if not Sent_msg.validation(data):
        return redirect("/output")
    Sent_msg.new_msg_sent(data)
    Rec_msg.new_msg_rec(data)
    return redirect("/output")