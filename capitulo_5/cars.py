cars = [
    'audi', 'bmw',
    'subaru', 'toyota'
]

for car in cars:
    if car == 'bmw':
        print(car.upper()) 
    else: 
        print(car.title())

print("\n")
car = 'bmw'
print(car == 'bmw')     # True
print(car == 'audit')   # False

print("\n")
car = 'Audit'
print(car == 'audit')           # False
print(car.lower() == 'audit')   # True