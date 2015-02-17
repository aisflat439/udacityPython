import turtle

s_distance = 100
s_degrees = 90
t_distance = 200
tri_degrees = 120
c_distance = 150

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

def moving_circle(t):
	x = 0
	y = 0
	for x in range(0,50):
		draw_circle(t)
		t.penup()
		t.goto(x,y)
		t.pendown()
		if y <= 90:
			x = x + 10
		elif y < (-90):
			x = x - 10
		if x <= 90:
			y = y + 10
		elif x < (-90):
			y = y - 10

window = turtle.Screen()
window.setup(900,900)
window.bgcolor("blue")

redTurtle = turtle.Turtle()
greenTurtle = turtle.Turtle()
whiteTurtle = turtle.Turtle()

whiteTurtle.speed(0)

redTurtle.color("red")
greenTurtle.color("green")
whiteTurtle.color("white")

draw_circle(redTurtle)
moving_circle(whiteTurtle)

window.exitonclick()