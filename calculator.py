"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )
#def calculator():
result = False
while result == False: 
    what_fxn = input("What would you like to compute? >")
    tokens = what_fxn.split(" ")
    if tokens[0] == "q":
        break
#add
    tokens[1] = int(tokens[1])
    tokens[2] = int(tokens[2])

    if tokens[0] == "+":
        answer = add(tokens[1],tokens[2])
#subtract
    elif tokens[0] == "-":
        answer = subtract(tokens[1],tokens[2])
#multiply
    elif tokens[0] == "*":
        answer =  multiply(tokens[1],tokens[2])
#divide
    elif tokens[0] == "/":
        answer = divide(tokens[1],tokens[2])
#square
    elif tokens[0] == "square":
        answer = square(tokens[1])
#cube
    elif tokens[0] == "cube":
        answer = cube(tokens[1])
#power
    elif tokens[0] == "pow":
        answer = power(tokens[1], tokens[2])
#mod
    elif tokens[0] == "mod":
        answer = mod(tokens[1], tokens[2])
    else:
        print("wrong! try again")
    print (answer)

