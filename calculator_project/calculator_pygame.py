import turtle

# Global variables to store input values
x_input = None
y_input = None

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y, decimal_places=2):
    if y == 0:
        return "Error: Division by zero!"
    result = x / y
    rounded_result = round(result, decimal_places)
    return rounded_result

# Set up main screen
screen = turtle.Screen()
screen.setup(width=500, height=500)
screen.title("Catculator")
screen.bgpic("background.gif")

# Function to set global input values
def set_input_values(x, y):
    global x_input, y_input
    x_input = x
    y_input = y

# Take input for x and y
x_input = float(turtle.numinput("Enter the first number", "Enter a number"))
y_input = float(turtle.numinput("Enter the second number", "Enter a number"))

# Register shapes
screen.register_shape("addition.gif")
screen.register_shape("subtraction.gif")
screen.register_shape("divide.gif")
screen.register_shape("multiplication.gif")

# Create image turtles for operations
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

# Function to display answer
def display_answer(result):
    screen.clear()  # Clear the main screen
    answer_screen = turtle.Screen()  # Create a new answer screen
    answer_screen.setup(width=300, height=100)
    answer_screen.title("Answer")
    
    answer_turtle = turtle.Turtle()
    answer_turtle.hideturtle()
    answer_turtle.penup()
    answer_turtle.goto(0, 0)
    answer_turtle.write(f"Answer: {result}", align="center", font=("Arial", 24, "normal"))

# Define click actions
def add_click(x, y):
    result = add(x_input, y_input)
    display_answer(result)

def subtract_click(x, y):
    result = subtract(x_input, y_input)
    display_answer(result)

def divide_click(x, y):
    result = divide(x_input, y_input)
    display_answer(result)

def multiply_click(x, y):
    result = multiply(x_input, y_input)
    display_answer(result)

# Assign click actions to turtles
addition_turtle.onclick(lambda x, y: add_click(x, y))
subtraction_turtle.onclick(lambda x, y: subtract_click(x, y))
divide_turtle.onclick(lambda x, y: divide_click(x, y))
multiplication_turtle.onclick(lambda x, y: multiply_click(x, y))

screen.mainloop()
