age = int(input("Enter age: "))

if age < 4:
    admission = 0
elif age < 18:
    admission = 5
else:
    admission = 10

print("Admission is $" + str(admission))