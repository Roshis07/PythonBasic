def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"

def square(a):
    return a ** 2

def cube(a):
    return a ** 3

def main():
    x = float(input("Enter a number (x): "))
    y = float(input("Enter another number (y): "))

    print(f"Addition: {x} + {y} = {add(x, y)}")
    print(f"Subtraction: {x} - {y} = {subtract(x, y)}")
    print(f"Multiplication: {x} * {y} = {multiply(x, y)}")
    
    if y != 0:
        print(f"Division: {x} / {y} = {divide(x, y)}")
    else:
        print("Cannot perform division by zero.")

    print(f"Square of {x}: {square(x)}")
    print(f"Cube of {y}: {cube(y)}")

if __name__ == "__main__":
    main()
