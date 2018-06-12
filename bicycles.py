# 2018-05-21
# First look at Python lists in awhile;
# Source: Python Crash Course (38f)
# Developed: Pydroid3, WingIDE;
# 646e62

# ---------
# FUNCTIONS
# ---------

# This function is designed to evaluate a yes/no response and return a value. It takes a "question string" as input (eg, "Abort?" or "Continue?").

def yes_no(question_string):
	
	answer = input(question_string)
	return_value = "X"
	
	if answer == "y" or "Y":
		return_value = "Y"
	elif answer == "n" or "N":
		return_value = "N"
	else:
		print(question_string)

# List variable
bicycles = ['trek', 'cannondale', 'redline', 'specialized', 'mountain']

# item = input("Item: ")
# bicycles.append(item)

# bicycles.append("item") will add new items to the end of the list.
# bicycles.insert(position, item) will add new items to a specified point in the list.


# This segment assigns an index number, and runs through the /bicycles/ list. The search is still rudimentary. It should be able to examine the list's length and assign a search number value from there.

# This bit of code creates a basic search and display function
count = 0

while count <= len(bicycles) - 1:
	print(str(count + 1) + ". " + bicycles[count].title())
	count += 1