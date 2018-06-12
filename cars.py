cars = ['audi', 'bmw', 'gm', 'subaru', 'toyota']

for car in cars:
    if car == "bmw" or car == "gm":
        print(car.upper())
    else:
        print(car.title())

print("gm" in cars)