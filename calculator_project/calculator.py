import turtle

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

# Set up screen
screen = turtle.Screen()
screen.setup(width=500, height=500)
screen.title("Catculator")

# Take input for x and y
x = turtle.textinput("Enter the first number", "Enter a number")
y = turtle.textinput("Enter the second number", "Enter a number")

# Turn into floats
x = float(x)
y = float(y)

# Register shapes
screen.register_shape("addition.gif")
screen.register_shape("subtraction.gif")
screen.register_shape("divide.gif")
screen.register_shape("multiplication.gif")

# Create image turtles
addition_turtle = turtle.Turtle()
subtraction_turtle = turtle.Turtle()
divide_turtle = turtle.Turtle()
multiplication_turtle = turtle.Turtle()

# Set positions for the image turtles
addition_turtle.shape("addition.gif")
addition_turtle.penup()
addition_turtle.goto(-140, 80)

subtraction_turtle.shape("subtraction.gif")
subtraction_turtle.penup()
subtraction_turtle.goto(140, 80)

divide_turtle.shape("divide.gif")
divide_turtle.penup()
divide_turtle.goto(-140, -140)

multiplication_turtle.shape("multiplication.gif")
multiplication_turtle.penup()
multiplication_turtle.goto(140, -140)

# Keep the window open
turtle.done()
