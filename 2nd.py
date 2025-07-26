import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Neon Snake 🐍")

# Create the snake's head
snake = turtle.Turtle()
snake.shape("circle")
snake.color("lime")  
snake.penup()
snake.speed(0)

# Function to move snake randomly
def move_snake():
    colors = ["red", "orange", "yellow", "green", "cyan", "blue", "magenta"]
    snake.color(random.choice(colors))
    angle = random.randint(0, 360)
    snake.setheading(angle)
    snake.forward(20)
    screen.ontimer(move_snake, 100)
    



# Start the animation
move_snake()

# Keep the window open
screen.mainloop()