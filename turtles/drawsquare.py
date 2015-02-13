import turtle

distance = 100
degrees = 90
pen_size = 10
tri_degrees = 120

def draw_square():
	devin = turtle.Turtle()
	devin.shape("turtle")
	devin.shapesize(3,3,5)
	devin.color("blue")
	devin.speed(1)

	for x in range(0,4):
		devin.forward(distance)
		devin.right(degrees)

def draw_circle():
	sarah = turtle.Turtle()
	sarah.shape("arrow")
	sarah.color("green")
	sarah.pensize(pen_size)
	sarah.circle(distance)

def draw_triangle():
	tuna = turtle.Turtle()
	tuna.speed(3)
	tuna.color("white")

	for x in range(0,3):
		tuna.forward(distance)
		tuna.left(tri_degrees)

window = turtle.Screen()
window.bgcolor("red")

draw_square()
draw_circle()
draw_triangle()

window.exitonclick()
