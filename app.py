from flask import Flask,Response
from dotenv import load_dotenv
load_dotenv()
import os
app=Flask(__name__)

# print(os.getenv("HOST"))
@app.route("/")
def welcome():
    return "HEllo word"

@app.route("/home")
def home():
    return "This is home page"

@app.route("/test")
def test():
    return "this is a test route"

# from controller import product_controller,user_controller
from controller import *

if __name__=='__main__':
    app.run(host="0.0.0.0",debug=True)
