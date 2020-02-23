import turtle

# Window
window = turtle.Screen()
window.title("Pong by malte9202")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

# Paddle A
paddle_a = turtle.Turtle()  # turtle object
paddle_a.speed(0)  # sets maximum speed
paddle_a.shape("square")  # defines shape
paddle_a.color("white")  # defines color
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()  # turtle object
paddle_b.speed(0)  # sets maximum speed
paddle_b.shape("square")  # defines shape
paddle_b.color("white")  # defines color
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()  # turtle object
ball.speed(0)  # sets maximum speed
ball.shape("square")  # defines shape
ball.color("white")  # defines color
ball.penup()
ball.goto(0, 0)
ball.dx = 0.25  # Try different numbers, ball always moves that many pixels
ball.dy = 0.25  # Try different numbers, ball always moves that many pixels


# Functions to move paddles up and down
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


# Keyboard binding
window.listen()
window.onkeypress(paddle_a_up, "w")
window.onkeypress(paddle_a_down, "s")
window.onkeypress(paddle_b_up, "Up")  # arrow up
window.onkeypress(paddle_b_down, "Down")  # arrow down

# Main game loop
while True:
    window.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:  # check if ball hits the border
        ball.sety(290)  # pin y coordinate
        ball.dy *= -1  # reverses the direction

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() < 