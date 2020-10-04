requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("Hold the anchovies!")

print("\n")
requested_topping = [
    'mushrooms', 'onions', 'pineapple'
]

print('mushrooms' in requested_topping)
print('pepperoni' in requested_topping)

# Testando várias condições
print("\n")

requested_toppings = [
    'mushrooms', 'extra cheese'
]
# Se mais de um bloco de código deve executar
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")

if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")

if 'extra cheese' in requested_toppings:
    print("Adding extra cheese")

if 'extra cheese' in requested_toppings:
    print("\nFinished making your pizza!")

# Se quiser que apenas um bloco de código seja executado
print("\n")
if 'mushrooms' in requested_toppings: 
    print("Adding mushrooms.") 
elif 'pepperoni' in requested_toppings:
    print("Adding pepperoni.") 
elif 'extra cheese' in requested_toppings: 
    print("Adding extra cheese.")

print("\nFinished making your pizza!")