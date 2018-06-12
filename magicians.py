import sys

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favourite foods are: ")
for value in my_foods:
    print("    " + "* " + value.title())
    
print("\nMy friend's favourite foods are: ")
for friend_foods in friend_foods[0:]:
    print("    " + "* " + friend_foods.title())
    
print(sys.platform)