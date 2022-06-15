from distutils.log import debug
from itertools import count
from flask import Flask, render_template, redirect,request, session


app = Flask(__name__)

app.secret_key ="cool_counter"

@app.route("/")
def index():
    if "act_visits" not in session:
        session["act_visits"] = 1
    else:
        session["act_visits"] +=1
        
    if "counter"not in session:
        session["counter"] = 1
    else:
        session["counter"] +=1
    return render_template("index.html")

@app.route("/counter/<int:visits>")
def manupulate_counter (visits):
    if visits ==1:
        return redirect("/")
    elif visits ==2:
        session["counter"] +=1
        return redirect("/")

@app.route("/destroy_session")
def destroy_session ():
    session.pop("counter") 
    return redirect("/")

@app.route('/add_count', methods=['POST'])         
def add_count():
    session["counter"] += (int(request.form["count"])-1)
    return  redirect("/")


@app.route("/handle_form", methods = ["POST"])
def handle_form_input():
    
    return redirect("/")

if __name__ =="__main__":
    app.run(debug = True)