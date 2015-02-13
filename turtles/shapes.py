import turtle

s_distance = 100
s_degrees = 90
t_degrees = 20

def draw_square(t):
	for x in range(0,4):
		t.forward(s_distance)
		t.right(s_degrees)

def circle_square(t):
	for x in range(0,18):
		draw_square(t)
		t.right(t_degrees)

window = turtle.Screen()
window.bgcolor("red")
	
devin = turtle.Turtle()
devin.color("green")

circle_square(devin)

window.exitonclick()