from flask import Flask, render_template  # Import Flask to allow us to create our app


app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return render_template()  # Return the string 'Hello World!' as a response


@app.route('/multitable/<int:x>/<int:x>')
def multification_table(x,y):
    result = []
    
    for i in range (0,x+1):
        new_list = []
        for j in range(0,y+1):
            new_list.append(i*j)
        result.append(new_list)          
    print (result)

    return render_template("table.html", x=x , y=y, result= result)
    


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

