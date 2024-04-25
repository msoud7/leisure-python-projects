import turtle
import time
import pygame

# Load images and sounds outside functions
focus_bg = "focus.png"
break_bg = "break.png"
pygame.mixer.init()
splat_sound = pygame.mixer.Sound("splat.mp3")
egg_timer_sound = pygame.mixer.Sound("egg_timer.mp3")

def draw_timer(timer_turtle, minutes, seconds, text):
    timer_turtle.clear()
    timer_turtle.goto(0, -20)
    
    # Draw text outline in black
    timer_turtle.pencolor("black")
    timer_turtle.write(f"{minutes:02}:{seconds:02}", align="center", font=("Comic Sans MS", 84, "bold"))
    
    # Draw final text in white (centered on top of the black outline)
    timer_turtle.goto(0, -20)
    timer_turtle.pencolor("white")
    timer_turtle.write(f"{minutes:02}:{seconds:02}", align="center", font=("Comic Sans MS", 80, "bold"))

def countdown_timer(timer_turtle, duration, text):
    for x in range(duration, -1, -1):
        minutes = x // 60
        seconds = x % 60
        draw_timer(timer_turtle, minutes, seconds, text)
        time.sleep(1)

def pomodoro_cycle(screen, timer_turtle, focus_time, break_time):
    while True:
        # Focus time
        screen.bgpic(focus_bg)
        splat_sound.play()
        countdown_timer(timer_turtle, focus_time * 60, "Focus Time")

        # Pause between shifts
        egg_timer_sound.play()

        # Break time
        screen.bgpic(break_bg)
        countdown_timer(timer_turtle, break_time * 60, "Break Time")

def main():
    # Set up turtle screen and tomato background
    screen = turtle.Screen()
    screen.setup(width=600, height=600)
    screen.title("Pomodoro Timer")

    # Take input for focus time and break time
    focus_time_str = turtle.textinput("Focus Time", "Enter focus time in minutes:")
    break_time_str = turtle.textinput("Break Time", "Enter break time in minutes:")
    
    # Convert input strings to integers
    focus_time = int(focus_time_str) if focus_time_str else 25  # Default to 25 minutes
    break_time = int(break_time_str) if break_time_str else 5  # Default to 5 minutes

    timer_turtle = turtle.Turtle()
    timer_turtle.hideturtle()
    timer_turtle.penup()
    timer_turtle.color("white")
    timer_turtle.goto(0, -250)

    while True:
        pomodoro_cycle(screen, timer_turtle, focus_time, break_time)

    screen.mainloop()

if __name__ == "__main__":
    main()
