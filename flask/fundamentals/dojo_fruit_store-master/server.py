from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    print ("charging " + request.form["first_name"] + " for " + str(int(request.form["apple"])+int(request.form["raspberry"])+int(request.form["strawberry"]))+" items.")
    return  render_template("checkout.html",
                            apple = request.form["apple"],
                            raspberry = request.form["raspberry"], 
                            strawberry = request.form["strawberry"], 
                            first_name = request.form["first_name"], 
                            last_name = request.form["last_name"], 
                            student_id = request.form["student_id"],)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    