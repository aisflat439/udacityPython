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

window = turtle.Screen()
window.setup(900,900)
window.bgcolor("blue")

redTurtle = turtle.Turtle()
greenTurtle = turtle.Turtle()
whiteTurtle = turtle.Turtle()

redTurtle.color("red")
greenTurtle.color("green")
whiteTurtle.color("white")

draw_square(whiteTurtle)
draw_circle(redTurtle)
draw_triangle(greenTurtle )

window.exitonclick()