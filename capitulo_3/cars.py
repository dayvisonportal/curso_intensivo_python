cars = ['bmw','audi','toyota','subaru']
cars.sort()
print(cars)

cars.sort(reverse=True)
print(cars)

cars.clear()
cars = ['bmw','audi','toyota','subaru']

print("\nHere is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)

cars.reverse()
print(cars)

print(len(cars))