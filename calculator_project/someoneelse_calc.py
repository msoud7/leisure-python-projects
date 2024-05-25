import turtle

def operate(operation, x, y):
    try:
        result = operation(x, y)
        result_turtle.clear()
        result_turtle.write(f"Result: {result}", align="center", font=("Arial", 24, "bold"))
    except ZeroDivisionError:
        result_turtle.clear()
        result_turtle.write("Error: Division by zero!", align="center", font=("Arial", 24, "bold"))

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ZeroDivisionError("Error: Division by zero!")
    return x / y

# Set up screen
screen = turtle.Screen()
screen.setup(width=500, height=500)
screen.title("Catculator")

# Register shapes and create result turtle
screen.register_shape("addition.gif")
screen.register_shape("subtraction.gif")
screen.register_shape("divide.gif")
screen.register_shape("multiplication.gif")
result_turtle = turtle.Turtle()
result_turtle.hideturtle()
result_turtle.penup()
result_turtle.goto(0, 200)

def get_input(prompt):
    value = float(turtle.textinput(prompt, "Enter a number"))
    return value

def setup_button(shape, position, operation, input_prompt):
    button = turtle.Turtle()
    button.shape(shape)
    button.penup()
    button.goto(position)
    button.onclick(lambda x=input_prompt: operate(operation, x(), get_input("Enter the second number")))

# Create image turtles and set positions
operations = [
    ("addition.gif", (-140, 80), add, lambda: get_input("Enter the first number")),
    ("subtraction.gif", (140, 80), subtract, lambda: get_input("Enter the first number")),
    ("divide.gif", (-140, -140), divide, lambda: get_input("Enter the first number")),
    ("multiplication.gif", (140, -140), multiply, lambda: get_input("Enter the first number"))
]

for shape, position, operation, input_prompt in operations:
    setup_button(shape, position, operation, input_prompt)

# Keep the window open
turtle.done()
