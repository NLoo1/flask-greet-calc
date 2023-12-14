
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

@app.route("/math/<operator>")
def all_in_one(operator):
    operator = operator.lower()
    numbers = request.args
    a = int(numbers['a'])
    b = int(numbers['b'])

    dct = {
        'add': add(a,b),
        'sub': sub(a,b),
        'mult': mult(a,b),
        'div': div(a,b)
    }

    operation = dct.get(operator)
    return str(operation)
    