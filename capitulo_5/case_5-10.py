# 5.10 Verificando nomes de usuários
current_users = [
    'admin', 'user a', 'user b', 
    'user c', 'user d', 'user e'
]

new_users = [
    'user d', 'user e', 'user x',
    'user y', 'user z', 'user w'
]

for new_user in new_users:
    if new_user.lower() in current_users:
        print(new_user + ", forneça um novo nome de usuário!")
    else:
        print(new_user + ", este nome de usuário está disponível.")