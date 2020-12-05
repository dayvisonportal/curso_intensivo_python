# Usando um laço while com listas e dicionários
# Transferindo itens de uma lista para outra

# Começa com os usuários que precisam ser verificados,
# e com uma lista vazia para armazenar os usuários confirmados
unconfimed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# Verifica cada usuário até que não haja mais usuários não confirmados
# Transfere cada usuário verificado para a lista de usuários confirmados
while unconfimed_users:
    # Nesse laço, a função pop() remove os usuários não
    # verificados, um de cada vez, do final de unconfirmed_users
    current_user = unconfimed_users.pop()
    print("\nVerifying user: " + current_user.title())
    confirmed_users.append(current_user)
    # Exibe todos os usuários confirmados
    print("\nThe following users have been confirmed:")
    for confirmed_user in confirmed_users:
        print(confirmed_user.title())
