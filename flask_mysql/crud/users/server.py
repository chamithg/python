from cgi import print_arguments
from flask import Flask, render_template,request,redirect
# import the class from friend.py
from users import User
app = Flask(__name__)
@app.route("/")
def index():
    # call the get all classmethod to get all friends
    users = User.get_all()
    print(users)
    return render_template("all_users.html", users = users)


# relevant code snippet from server.py
from users import User
@app.route('/create', methods=["POST"])
def create_user():
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    data = {
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "email" : request.form["email"]
    }
    # We pass the data dictionary into the save method from the Friend class.
    print(data)
    User.save(data)
    # Don't forget to redirect after saving to the database.
    return redirect('/')

@app.route('/all')
def view():
    return render_template("show_user.html",users = User.get_all())
            
@app.route('/show/<int:id>')
def show(id):
    data={"id":id }
    return render_template("show_user.html",num = id, user = User.get_one(data))

@app.route('/update/<int:id>' , methods=["POST"])
def update(id):
    data={"id":id, 
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "email" : request.form["email"] }
    User.update(data)
    return redirect("/")

@app.route('/edit/<int:id>' )
def edit(id):
    data={"id":id }
    return render_template("edit_user.html", user = User.select_update(data))
            
@app.route('/delete/<int:id>')
def delete(id):
    data={"id":id }
    User.delete(data)
    return redirect("/")
            
@app.route('/new')
def create():
    return render_template("new_user.html")
            
if __name__ == "__main__":
    app.run(debug=True)

 