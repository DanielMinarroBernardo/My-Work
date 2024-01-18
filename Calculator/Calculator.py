import math
import sys

def main():
    print("\nWhat operation do you want to perform?")
    print("1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Exponentiate\n6. Square Root\n7. Logarithm\n8. Modulo")
    
    op = int(input("Enter the number of the operation you want to perform: "))
    #Call the Operation method
    Operation(op)


#This method is so that the program can be repeated and perform another calculation without having to close and run it again.
def Repeat(rep):
    if rep == 1:
        main()
    else:
        sys.exit()

#This method evaluates the user's input so that depending on the operation they want to perform, they are redirected to that operation.
def Operation(op):
    if op == 1:
        Add()
    elif op == 2:
        Subtract()
    elif op == 3:
        Multiply()
    elif op == 4:
        Divide()
    elif op == 5:
        Exponentiate()
    elif op == 6:
        SquareRoot()
    elif op == 7:
        Logarithm()
    elif op == 8:
        Module()
    else:
        print("Invalid operation")

#This method adds 2 values
def Add():
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    calc = a + b
    print("The result of the addition is:", calc)
    print("\nDo you want to perform another operation?")
    print("1. Yes\n2. No")
    rep = int(input("Enter the number of the action to perform: "))
    Repeat(rep)

#This method substracts 2 values
def Subtract():
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    calc = a - b
    print("The result of the subtraction is:", calc)
    print("\nDo you want to perform another operation?")
    print("1. Yes\n2. No")
    rep = int(input("Enter the number of the action to perform: "))
    Repeat(rep)

#This method multiplys 2 values
def Multiply():
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    calc = a * b
    print("The result of the multiplication is:", calc)
    print("\nDo you want to perform another operation?")
    print("1. Yes\n2. No")
    rep = int(input("Enter the number of the action to perform: "))
    Repeat(rep)

#This method divides 2 values
def Divide():
    a = float(input("Enter the numerator: "))
    b = float(input("Enter the denominator: "))
    if b != 0:
        calc = a / b
        print("The result of the division is:", calc)
    else:
        print("Error: Cannot divide by zero.")
    print("\nDo you want to perform another operation?")
    print("1. Yes\n2. No")
    rep = int(input("Enter the number of the action to perform: "))
    Repeat(rep)

#This method raises 1 value by the exponent
def Exponentiate():
    a = float(input("Enter the base: "))
    b = float(input("Enter the exponent: "))
    calc = math.pow(a, b)
    print("The result of raising", a, "to the power of", b, "is:", calc)
    print("\nDo you want to perform another operation?")
    print("1. Yes\n2. No")
    rep = int(input("Enter the number of the action to perform: "))
    Repeat(rep)

#This method does the square root of a value
def SquareRoot():
    a = float(input("Enter the number to calculate the square root: "))
    calc = math.sqrt(a)
    print("The square root of", a, "is:", calc)
    print("\nDo you want to perform another operation?")
    print("1. Yes\n2. No")
    rep = int(input("Enter the number of the action to perform: "))
    Repeat(rep)

#This method does the logarithm of a value
def Logarithm():
    a = float(input("Enter the number to calculate the natural logarithm: "))
    calc = math.log(a)
    print("The natural logarithm of", a, "is:", calc)
    print("\nDo you want to perform another operation?")
    print("1. Yes\n2. No")
    rep = int(input("Enter the number of the action to perform: "))
    Repeat(rep)

#This method calculate de module of 2 values
def Module():
    a = float(input("Enter the number: "))
    b = float(input("Enter the divisor: "))
    calc =  a % b
    print("The result of the modulo of", a, "over", b, "is:", calc)
    print("\nDo you want to perform another operation?")
    print("1. Yes\n2. No")
    rep = int(input("Enter the number of the action to perform: "))
    Repeat(rep)

#This is the main script that executes the program
if __name__ == "__main__":
    # Call the main method
    main()
