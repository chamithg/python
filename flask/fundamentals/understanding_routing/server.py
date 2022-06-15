from flask import Flask

app = Flask(__name__)    

@app.route('/')          
def hello_world():
    return 'Hello World!'  

@app.route('/dojo')          
def dojo():
    return 'Dojo'  

@app.route('/say/<string:anyString>')          
def say(anyString):
    return f"hi {anyString}"  

@app.route('/repeat/<int:times>/<string:anyString>')          
def repeat(anyString ,times):
    return f"{anyString  * times  }" 


if __name__=="__main__":   
    app.run(debug=True)    

