# 7.8 Lanchonete
sandwich_orders = ['sanduba a', 'sanduba b', 'sanduba c']
finished_sandwiches = []

# Para cada valor contido na lista sandwich_orders
while sandwich_orders:
    # Inserir na variavel sandwich o ultimo item que foi
    # retirado de sandwich_orders
    sandwich = sandwich_orders.pop()
    print("Preparei seu " + sandwich.title() + ".")
    # Inserir na ultima posição da lista finished_sandwiches
    # a variavel sandwich
    finished_sandwiches.append(sandwich)

print(finished_sandwiches)
