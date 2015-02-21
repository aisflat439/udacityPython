class Parent():
	def __init__(self, last_name, eye_color):
		print("Parent constructor called")
		self.last_name = last_name
		self.eye_color = eye_color

class Child(Parent):
	"""Inherits from Parent"""
	def __init__(self, last_name, eye_color, num_toys):
		print("Child constructor called")
		Parent.__init__(self, last_name, eye_color)
		self.num_toys = num_toys
		
# billy = Parent("cyrus", "blue")
# print(billy.eye_color)
miley = Child("cyrus", "blue", 5)
print(miley.eye_color)
print(miley.num_toys)
