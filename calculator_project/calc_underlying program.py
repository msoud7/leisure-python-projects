#create the formulas
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero!"
    return x / y

x = float(input("Enter your first number: "))
y = float(input("Enter your second number: "))

choice = input("Which operator would you like to use? (+,-,*,/): ")

if choice == "+":
    print(add(x, y))
elif choice == "-":
    print(subtract(x, y))
elif choice == "*":
    print(multiply(x, y))
elif choice == "/":
    print(divide(x, y))

