import turtle

s_distance = 100
s_degrees = 90
t_distance = 200
tri_degrees = 120
c_distance = 150
pen_size = 10

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
window.bgcolor("red")

tuna = turtle.Turtle()
devin = turtle.Turtle()
sarah = turtle.Turtle()

sarah.color("green")
tuna.color("white")
devin.color("blue")

draw_square(sarah)
draw_circle(devin)
draw_triangle(tuna)

window.exitonclick()
