#!/usr/bin/env python3

from flask import Flask


app = Flask(__name__)

if __name__ == '__main__':
    app.run(port=5555, debug=True)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string_parameter>')
def print_string(string_parameter):
    print(f"Received string: {string_parameter}")
    return string_parameter

@app.route('/count/<int:count_parameter>')
def count_route(count_parameter):
    result = '\n'.join(map(str, range(count_parameter)))
    return result


@app.route('/math/<float:num1><operation><float:num2>')
def math(num1, operation, num2):
    result = None

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 != 0:
            result = num1 / num2
    elif operation == '%':
        result = num1 % num2

    return str(result)
