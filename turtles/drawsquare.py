import turtle

distance = 100

def draw_square():
	window = turtle.Screen()
	window.bgcolor("red")

	devin = turtle.Turtle()
	devin.shape("turtle")
	devin.shapesize(3,3,5)
	devin.color("blue")
	devin.speed(1)

	for x in range(0,4):
		devin.forward(distance)
		devin.right(90)

	sarah = turtle.Turtle()
	sarah.shape("arrow")
	sarah.color("green")
	sarah.pensize(10)
	sarah.circle(100)

	window.exitonclick()

draw_square()
