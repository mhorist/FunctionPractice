# Write a Python program to execute a string containing Python code.

def math(x, y):
    print(x * y)
    op = input("Enter an operator (+, -, *, /): ")
    if op == "+":
        print(x + y)
    elif op == "-":
        print(x - y)
    elif op == "*":
        print(x * y)
    elif op == "/":
        print(x / y)
    else:
        print("Invalid Input.")

# getting an error here.  I need to figure out how to convert my arg from a str to an int...
# this one has stumped me for a bit...
# stack overflow not helping
x = input(int("Enter a number: "))
y = input(int("Enter another number: "))
math(x, y)