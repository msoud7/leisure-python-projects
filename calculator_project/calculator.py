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
screen = turtle.Screen() #initialize the base
screen.setup(width=500, height=500) #set the size of the base
screen.title("Catculator") #name the application

# Take input for x and y
x = turtle.textinput("Enter the first number", "Enter a number")
y = turtle.textinput("Enter the second number", "Enter a number")

# Turn into floats
x = float(x)
y = float(y)

# Register shapes
screen.register_shape("addition.gif") #register size
screen.register_shape("subtraction.gif")
screen.register_shape("divide.gif")
screen.register_shape("multiplication.gif")

# Create image turtles
addition_turtle = turtle.Turtle() #create base shape 1
subtraction_turtle = turtle.Turtle() #create base shape 2
divide_turtle = turtle.Turtle() #create base shape 3
multiplication_turtle = turtle.Turtle() #create base shape 4

# Set positions for the image turtles
addition_turtle.shape("addition.gif") #add the gif to the base shape
addition_turtle.penup() #stop drawing
addition_turtle.goto(-140, 80) #displace
addition_turtle.onclick(add)

subtraction_turtle.shape("subtraction.gif")
subtraction_turtle.penup()
subtraction_turtle.goto(140, 80)
subtraction_turtle.onclick(subtract)

divide_turtle.shape("divide.gif")
divide_turtle.penup()
divide_turtle.goto(-140, -140)
divide_turtle.onclick(divide)

multiplication_turtle.shape("multiplication.gif")
multiplication_turtle.penup()
multiplication_turtle.goto(140, -140)
multiplication_turtle.onclick(multiply)

# Keep the window open
turtle.done()
