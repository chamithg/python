from distutils.log import debug
from flask import Flask


app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World!"

@app.route("/success")
def success():
    return "Success!"

@app.route("/hello/<anyString>")  
def hello(anyString):
    return f"Hello {anyString}"
#!---> by default this any part is "string" if we expecting another data type we need to specify it.

@app.route("/age/<int:anyint1>/<int:anyint2>")  
def age(anyint1, anyint2):
    return f"your age is years:{anyint1} months: {anyint2}"
 




if __name__=="__main__":
    app.run(debug= True)