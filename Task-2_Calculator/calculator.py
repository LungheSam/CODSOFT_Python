"""
    BASIC CALCULATOR By Samuel Lunghe 
"""
import math

def addition(a,b):
    print("*"*15+' Result '+"*"*15)
    print(f"{a}+{b}={a+b}")
    print("*"*40)
    return a+b
def subtraction(a,b):
    print("*"*15+' Result '+"*"*15)
    print(f"{a}-{b}={a-b}")
    print("*"*40)
    return a-b
def multiplication(a,b):
    print("*"*15+' Result '+"*"*15)
    print(f"{a}*{b}={a*b}")
    print("*"*40)
    return a*b
def division(a,b):
    try:
        c=a/b
        print("*"*15+' Result '+"*"*15)
        print(f"{a}/{b}={a/b}")
        print("*"*40)
    except ZeroDivisionError:
        print("Invalid Operation: Division By Zero")
        return None
    return c
def main():
    print("*"*40)
    print("="*10+"BASIC CALCULATOR"+"="*10)
    try:
        first_number=int(input("Enter the first number:"))
        second_number=int(input("Enter the second number:"))
    except Exception as e:
        print("Invalid Input")
        return None

    print("="*10+"OPERATIONS"+"="*10)
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print('='*40)
    try: 
        operation=int(input("Choose your operation (1,2...):"))

    except Exception as e:
        print("Invalid Input")
        return None
    try:
        match operation:
            case 1:
                print("*"*40)
                print("Addition")
                addition(first_number,second_number)
            case 2:
                print("*"*40)
                print("Subtraction")
                subtraction(first_number,second_number)
            case 3:
                print("*"*40)
                print("Multiplication")
                multiplication(first_number,second_number)
            case 4:
                print("*"*40)
                print("Division")
                division(first_number,second_number)
            case _:
                print("*"*40)
                print("Operation not Recognized")
                print("*"*40)
    except Exception as e:
        print("Invalid Input for Operation")
        return None

main()