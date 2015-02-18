import turtle

s_distance = 100
s_degrees = 90
t_distance = 100
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

def draw_right_leaf(t):
	for x in range(0,3):
		t.forward(t_distance)
		t.left(tri_degrees)

def draw_left_leaf(t):
	for x in range(0,3):
		t.backward(t_distance)
		t.right(tri_degrees)

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

def draw_stem(t):
	myTurtle.penup()
	myTurtle.goto(btx, bty)
	myTurtle.pendown()
	myTurtle.pensize(8)
	myTurtle.goto(btx,-350)

window = turtle.Screen()
window.setup(900,900)
window.bgcolor("blue")

myTurtle = turtle.Turtle()
myTurtle.speed(0)

for y in range(0,10):
	gx+=1
	gy+=1
	for x in range(0,10):
		myTurtle.color("white")
		draw_circle(myTurtle)
		move_turtle_right(myTurtle)
		move_turtle_up(myTurtle)
		btx = myTurtle.xcor()
		bty = myTurtle.ycor()
	for x in range(0,10):
		myTurtle.color("red")
		draw_circle(myTurtle)
		move_turtle_down(myTurtle)
		move_turtle_right(myTurtle)
	for x in range(0,10):
		myTurtle.color("green")
		draw_circle(myTurtle)
		move_turtle_down(myTurtle)
		move_turtle_left(myTurtle)
	for x in range(0,10):
		myTurtle.color("yellow")
		draw_circle(myTurtle)
		move_turtle_up(myTurtle)
		move_turtle_left(myTurtle)

draw_stem(myTurtle)
myTurtle.color("green")
draw_right_leaf(myTurtle)
draw_left_leaf(myTurtle)

window.exitonclick()