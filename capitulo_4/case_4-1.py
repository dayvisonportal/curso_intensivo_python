# 4.1 Pizzas
pizzas_list = ['Pizza A', 'Pizza B', 'Pizza C']

for pizza in pizzas_list:
    print("Gosto do sabor da " + pizza + ".")

print("\nEu realmente adoro pizza!\n\n")    

# 4.11 Minhas pizzas, suas pizzas
friend_pizzas = pizzas_list[:]
pizzas_list.append('Pizza D')
friend_pizzas.append('Pizza X')
print("Minhas pizzas favoritas são:")

for my_pizza in pizzas_list:
    print(my_pizza.title())

for friend_pizza in friend_pizzas:
    print(friend_pizza.title())

# 4.2 Animais
animals_list = ['gato','cachorro','coelho']

for animal in animals_list:
    print("\nUm " + animal + " seria um ótimo animal de estimação!")

print("\nQualquer um desses animais seria um ótimo animal de estimação!")

