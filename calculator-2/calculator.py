"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


exit = False

while (exit != True):
    
    input_equation = input('Enter Your Equation:')
    tokens = input_equation.split(" ") #turn string floato array called tokens
    if tokens[0] == '+': 
        result = add(num1 = float(tokens[1]), num2 = float(tokens[2]))
        print(result)

    if tokens[0] == '-': 
        result = subtract(num1 = float(tokens[1]), num2 = float(tokens[2]))
        print(result)

    if tokens[0] == '*': 
        result = multiply(num1 = float(tokens[1]), num2 = float(tokens[2]))
        print(result)

    if tokens[0] == '/': 
        result = divide(num1 = float(tokens[1]), num2 = float(tokens[2]))
        print(result)
    
    if tokens[0] == 'square': 
        result = square(num1 = float(tokens[1]))
        print(result)
        
    if tokens[0] == 'cube': 
        result = cube(num1 = float(tokens[1]))
        print(result)

    if tokens[0] == 'pow': 
        result = power(num1 = float(tokens[1]), num2 = float(tokens[2]))
        print(result)

    if tokens[0] == 'mod': 
        result = mod(num1 = float(tokens[1]), num2 = float(tokens[2]))
        print(result)

    if tokens[0] == "q":
        print("You are done.")
        exit = True