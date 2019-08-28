import turtle

##########
# SCREEN #
##########
wn = turtle.Screen()
wn.bgcolor("black")
wn.setup(width=600, height=500)
wn.tracer(0)  # speeds up our game
###########
# OBJECTS #
###########
# Lane lines
start_line = turtle.Turtle()
start_line.shape("square")
start_line.shapesize(30, .1)
start_line.color("white")
start_line.penup()
start_line.goto(-100, 0)
# Lane one
line_one = turtle.Turtle()
line_one.shape("square")
line_one.shapesize(30, .1)
line_one.color("white")
line_one.penup()
line_one.goto(-50, 0)
# Lane two
line_two = turtle.Turtle()
line_two.shape("square")
line_two.shapesize(30, .1)
line_two.color("white")
line_two.penup()
line_two.goto(0, 0)
# Lane three
line_three = turtle.Turtle()
line_three.shape("square")
line_three.shapesize(30, .1)
line_three.color("white")
line_three.penup()
line_three.goto(50, 0)
# Lane four
line_four = turtle.Turtle()
line_four.shape("square")
line_four.shapesize(30, .1)
line_four.color("white")
line_four.penup()
line_four.goto(100, 0)
# Lane five
line_five = turtle.Turtle()
line_five.shape("square")
line_five.shapesize(30, .1)
line_five.color("white")
line_five.penup()
line_five.goto(150, 0)
# Lane six
line_six = turtle.Turtle()
line_six.shape("square")
line_six.shapesize(30, .1)
line_six.color("white")
line_six.penup()
line_six.goto(200, 0)
# Lane seven
line_seven = turtle.Turtle()
line_seven.shape("square")
line_seven.shapesize(30, .3)
line_seven.color("green")
line_seven.penup()
line_seven.goto(250, 0)
# Ball one
ball_one = turtle.Turtle()
ball_one.shape("circle")
ball_one.color("white")
ball_one.penup()
ball_one.goto(-75, 0)
ball_one.dy = 2
# Ball two
ball_two = turtle.Turtle()
ball_two.shape("circle")
ball_two.color("white")
ball_two.penup()
ball_two.goto(-25, 0)
ball_two.dy = -1.5
# Ball three
ball_three = turtle.Turtle()
ball_three.shape("circle")
ball_three.color("white")
ball_three.penup()
ball_three.goto(25, 0)
ball_three.dy = 1.2
# Ball four
ball_four = turtle.Turtle()
ball_four.shape("circle")
ball_four.color("white")
ball_four.penup()
ball_four.goto(75, 0)
ball_four.dy = 1.7
# Ball five
ball_five = turtle.Turtle()
ball_five.shape("circle")
ball_five.color("white")
ball_five.penup()
ball_five.goto(125, 0)
ball_five.dy = -1.1
# Ball six
ball_six = turtle.Turtle()
ball_six.shape("circle")
ball_six.color("white")
ball_six.penup()
ball_six.goto(175, 0)
ball_six.dy = 1
# Ball seven
ball_seven = turtle.Turtle()
ball_seven.shape("circle")
ball_seven.color("white")
ball_seven.penup()
ball_seven.goto(225,0)
ball_seven.dy = -1.4
# Pen
pen = turtle.Turtle()
pen.speed(-3)
pen.color("green")
pen.penup()
pen.hideturtle()
pen.goto(0, 0)
# Turtle
turtle = turtle.Turtle()
turtle.shape("turtle")
turtle.color("green")
turtle.penup()
turtle.goto(-125, 0)
#############
# FUNCTIONS #
#############
# Moving your turtle
def turtle_up():
	"""Will move turtle up using coordinate method"""
	y = turtle.ycor()
	y += 50
	turtle.sety(y)
def turtle_down():
	"""Will move turtle down using coordinate method"""
	y = turtle.ycor()
	y += -50
	turtle.sety(y)
def turtle_right():
	"""Will move turtle to the right using coordinate method"""
	x = turtle.xcor()
	x += 50
	turtle.setx(x)
def turtle_left():
	"""Will move turtle to the left using coordinate method"""
	x = turtle.xcor()
	x += -50
	turtle.setx(x)
def ball_boarder_bounce(ball_number):
	"""ball will bounce back at the boarder of the screen"""
	if (ball_number).ycor() > 240:
		(ball_number).sety(240)
		(ball_number).dy *= -1
	if (ball_number).ycor() < -240:
		(ball_number).sety(-240)
		(ball_number).dy *= -1
def ball_intersect(left_x, right_x, ball_number):
	"""Turtle will go back to start after colliding with a ball"""
	# left_x and right_x define the x coordinate range the turtle needs to be in
	if (turtle.xcor() > (left_x) and turtle.xcor() < (right_x)) and \
		((ball_number).ycor() < turtle.ycor() + 10 and \
			(ball_number).ycor() > turtle.ycor() - 10):
		turtle.goto(-125, 0)
def movement_for_level(level):
	"""Balls will move up and down"""
	ball_one.sety(ball_one.ycor() + ball_one.dy * (level))
	ball_two.sety(ball_two.ycor() + ball_two.dy * (level))
	ball_three.sety(ball_three.ycor() + ball_three.dy * (level))
	ball_four.sety(ball_four.ycor() + ball_four.dy * (level))
	ball_five.sety(ball_five.ycor() + ball_five.dy * (level))
	ball_six.sety(ball_six.ycor() + ball_six.dy * (level))
	ball_seven.sety(ball_seven.ycor() + ball_seven.dy * (level))
def main_game_loop(level):
	"""Plays main game loop at speed of 1"""
	# Moving the ball
	movement_for_level(level)
	# Ball bounce
	ball_boarder_bounce(ball_one)
	ball_boarder_bounce(ball_two)
	ball_boarder_bounce(ball_three)
	ball_boarder_bounce(ball_four)
	ball_boarder_bounce(ball_five)
	ball_boarder_bounce(ball_six)
	ball_boarder_bounce(ball_six)
	ball_boarder_bounce(ball_seven)
	# Turtle and ball intersect
	ball_intersect(-100, -50, ball_one)
	ball_intersect(-50, 0, ball_two)
	ball_intersect(0, 50, ball_three)
	ball_intersect(50, 100, ball_four)
	ball_intersect(100, 150, ball_five)
	ball_intersect(150, 200, ball_six)
	ball_intersect(200, 250, ball_seven)
	if (turtle.xcor() > 250):
		wn.clear()
		wn.bgcolor("white")
		pen.write("You Won!", align="center", font=("Courier", 48, "normal"))
############
# CONTROLS #
############
wn.listen()
wn.onkey(turtle_left, "Left")
wn.onkey(turtle_up, "Up")
wn.onkey(turtle_right, "Right")
wn.onkey(turtle_down, "Down")
# ###########
# GAME LOOP #
# ###########
while True:
	wn.update()
	main_game_loop(3)
