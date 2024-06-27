#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)
    return f'{parameter}'

@app.route('/count/<int:parameter>')
def count(parameter):
    result = ""
    for number in range(parameter):
        result += f'{number}\n' # the \n is the newline character to ensure each number is printed on a new line
    return result

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        return f'{num1 + num2}'
    elif operation == '-':
        return f'{num1 - num2}'
    elif operation == '*':
        return f'{num1 * num2}'
    elif operation == 'div':
        if num2 == 0:
            return 'Division by zero is not allowed' # remembering to handle division by 0
        return f'{num1 / num2}'
    elif operation == '%':
        if num2 == 0:
            return 'Modulo by zero is not allowed' # same here as before to handle modulo by 0
        return f'{num1 % num2}'
    else:
        return 'Invalid operation'
    

if __name__ == '__main__':
    app.run(port=5555, debug=True)
