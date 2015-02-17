import turtle

s_distance = 100
s_degrees = 90
t_distance = 200
tri_degrees = 120
c_distance = 150
gx=0
gy=0
btx = 0
bty = 0

def draw_square(t):
	for x in range(0,4):
		t.forward(s_distance)
		t.right(s_degrees)

def draw_circle(t):
	t.circle(c_distance)

def draw_triangle(t):
	for x in range(0,3):
		t.forward(t_distance)
		t.left(tri_degrees)

def move_turtle_up(t):
	global gy
	t.penup()
	t.goto(gx,gy)
	t.pendown()
	gy+=10

def move_turtle_down(t):
	global gy
	t.penup()
	t.goto(gx,gy)
	t.pendown()
	gy-=10

def move_turtle_right(t):
	global gx
	t.penup()
	t.goto(gx,gy)
	t.pendown()
	gx+=10

def move_turtle_left(t):
	global gx
	t.penup()
	t.goto(gx,gy)
	t.pendown()
	gx-=10

window = turtle.Screen()
window.setup(900,900)
window.bgcolor("blue")

myTurtle = turtle.Turtle()
blackTurtle = turtle.Turtle()
redTurtle.color("red")
greenTurtle.color("green")
whiteTurtle.color("white")
yellowTurtle.color("yellow")
blackTurtle.color("black")
whiteTurtle.speed(0)
redTurtle.speed(0)
greenTurtle.speed(0)
yellowTurtle.speed(0)
blackTurtle.speed(0)
blackTurtle.pensize(15)

for y in range(0,2):
	gx+=1
	gy+=1
	for x in range(0,10):
		draw_circle(whiteTurtle)
		move_turtle_right(whiteTurtle)
		move_turtle_up(whiteTurtle)
		# btx = whiteTurtle.xcor()
		# bty = wh
	for x in range(0,10):
		draw_circle(redTurtle)
		move_turtle_down(redTurtle)
		move_turtle_right(redTurtle)
	for x in range(0,10):
		draw_circle(greenTurtle)
		move_turtle_down(greenTurtle)
		move_turtle_left(greenTurtle)
	for x in range(0,10):
		draw_circle(yellowTurtle)
		move_turtle_up(yellowTurtle)
		move_turtle_left(yellowTurtle)

blackTurtle.penup()
btx = whiteTurtle.xcor()
bty = whiteTurtle.ycor()
blackTurtle.goto(btx, bty)
blackTurtle.pendown()
gy = -500
blackTurtle.goto(btx, gy)

window.exitonclick()