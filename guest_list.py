# 2018-05-21

list = ['Abraham Lincoln', 'Paul of Tarsus', 'Weena Mercator', 'HP Lovecraft', 'Atilla the Hun']

# Sorts the list in reverse alphabetical order
list.sort(reverse = True)

print("Initial guest list: \n")

# Search and display function as a "for" statement, rather than a "while" statement. This makes more sense, given the data structure, and also makes it easy to append the "." to the last item on the list. 

for count in range(len(list) - 1):
    print(str(count + 1) + ".\t" + list[count] + ";")

# Addresses the last item on the list, ends it with a period instead of a semicolon.
print(str(len(list)) + ".\t" + list[-1] + ".")

