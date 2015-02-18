# read in strings. 
# each word is one string.
# check the string vs a list for matching.
# if it has a curse then print(has a curse)
# else print("message")

def read_text():
	quotes = open("/home/devindesktop/Udacity/texts/quotes.txt")
	contents_of_file = quotes.read()
	print(contents_of_file)
	quotes.close()

read_text()