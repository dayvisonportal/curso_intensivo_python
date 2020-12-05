# 7.9 Sem pastrami
sandwich_orders = ['sanduba a', 'pastrami',
                   'sanduba b', 'pastrami', 'sanduba c', 'pastrami']
out_of_order = sandwich_orders[1]
finished_sandwiches = []

print("\nA lanchonete está sem " + out_of_order.title() + " no momento.")

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    if sandwich != out_of_order:
        finished_sandwiches.append(sandwich)

print(finished_sandwiches)
