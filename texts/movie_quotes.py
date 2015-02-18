# read in strings. 
# each word is one string.
# check the string vs a list for matching.
# if it has a curse then print(has a curse)
# else print("message")

import urllib

def read_text():
	quotes = open("/home/devindesktop/tmp/tswift.txt")
	contents_of_file = quotes.read()
	print(contents_of_file)
	quotes.close()
	check_profanity(contents_of_file)

def check_profanity(text):
	connection = urllib.urlopen("http://www.wdyl.com/profanity?q="+text)
	output = connection.read()
	connection.close()
	if "true" in output:
		print("Profanity alert!")
	elif "false" in output:
		print("this document has no curses")
	else:
		print("document read failure")

read_text()