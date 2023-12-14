# Put your app in here.

from flask import Flask, request 
from operations import *

app = Flask(__name__)

@app.route("/add")
def add_numbers():
    numbers = request.args
    a = int(numbers['a'])
    b = int(numbers['b'])
    output = add(a,b)
    return str(output)

@app.route("/sub")
def subtract_numbers():
    numbers = request.args
    a = int(numbers['a'])
    b = int(numbers['b'])
    output = sub(a,b)
    return str(output)

@app.route("/mult")
def mult_numbers():
    numbers = request.args
    a = int(numbers['a'])
    b = int(numbers['b'])
    output = mult(a,b)
    return str(output)

@app.route("/div")
def div_numbers():
    numbers = request.args
    a = int(numbers['a'])
    b = int(numbers['b'])
    output = div(a,b)
    return str(output)