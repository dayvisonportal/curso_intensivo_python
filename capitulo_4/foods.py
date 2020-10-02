# Copiando uma lista
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:") 
print(friend_foods)

my_foods.append('cannoli')
friend_foods.append('ice cream')
print("\n")
print(my_foods)
print(friend_foods)
print("\n")

# 4.12 Mais laços
for food in my_foods:
    print(food.title())

print("\n")

for friend_food in friend_foods:
    print(friend_food.title())