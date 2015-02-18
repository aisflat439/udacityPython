# simple prorgram that uses min to find the smallest. 
first_user_input = 0
second_user_input = 0
third_user_input = 0
the_min = 0

print("Please enter a number")
first_user_input = input()
print("Please enter another number")
second_user_input = input()
print("Please enter another number")
third_user_input = input()

the_min = min(first_user_input, second_user_input, third_user_input)
the_max = max(first_user_input, second_user_input, third_user_input)

numbers = [first_user_input, second_user_input, third_user_input]
for i, number in enumerate(numbers):
	print "Number {iteration} entered was {number}".format(iteration=i+1, number=number)

print("The smallest number you entered was: " + str(the_min))
print("The largest number you entered was: " + str(the_max))