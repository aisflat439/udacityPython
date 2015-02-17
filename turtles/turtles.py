import turtle

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

window.exitonclick()