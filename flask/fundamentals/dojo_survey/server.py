from flask import Flask,render_template,redirect,request,session

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/result", methods =["POST"])
def index1():
    session["name"] =request.form["name"]
    session["location"] =request.form["location"]
    session["languages"] =request.form["languages"]
    session["comments"] =request.form["comments"]
    return redirect("/output")

@app.route("/output")
def output():
    return render_template("result.html")

@app.route("/go_back")
def go_back():
    return redirect("/")

# @app.route('/users', methods=['POST'])
# def create_user():
#     print("Got Post Info")
#     # Here we add two properties to session to store the name and email
#     session['username'] = request.form['name']
#     session['useremail'] = request.form['email']
#     return redirect('/show')

if __name__ =="__main__":
    app.run(debug = True)
