#importing the libraries required for the game
import turtle
import os

#creating screen
win = turtle.Screen()
win.title("Ping Pong")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)

#scoring
score_a = 0  
score_b = 0

#adding paddles and the ball to the screen
#paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=0.5)
paddle_a.penup()
paddle_a.goto(-350,0)

#paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=0.5)
paddle_b.penup()
paddle_b.goto(350,0)

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0,0)
ball.dx = 0.3
ball.dy = 0.3

#ccreating pen for scoring
pen = turtle.Turtle()
pen.speed(0)
pen.color("green")
pen.penup()
pen.hideturtle()
pen.goto(0,280)
pen.write("Player A: 0   Player B: 0", align="center",font=("couruer", 10, "normal"))

#function for moving the paddles 
def paddle_a_up():
	y = paddle_a.ycor()
	y += 40
	paddle_a.sety(y)

def paddle_a_down():
	y = paddle_a.ycor()
	y -= 40
	paddle_a.sety(y)

def paddle_b_up():
	y = paddle_b.ycor()
	y += 40
	paddle_b.sety(y)

def paddle_b_down():
	y = paddle_b.ycor()
	y -= 40
	paddle_b.sety(y)

#keyboard binding to the game
win.listen()
win.onkeypress(paddle_a_up, "w")
win.onkeypress(paddle_a_down, "s")
win.onkeypress(paddle_b_up, "Up")
win.onkeypress(paddle_b_down, "Down")

#game loop
while True:
	win.update()
	
	# move the ball
	ball.setx(ball.xcor() + ball.dx)
	ball.sety(ball.ycor() + ball.dy)

	#Border bouncing is done through this
	if ball.ycor() > 295:
		ball.sety(295)
		ball.dy *= -1
		os.system("aplay bounce.wav&")
