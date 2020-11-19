# 5.8 Olá admin
users = [
    'admin', 'user a', 'user b', 
    'user c', 'user d', 'user e'
]

for user in users:
    if user == 'admin':
        print("Olá " + user.title() + ", gostaria de ver um relatório de status?")
    else:
        print("Olá " + user.title() + ", obrigado por fazer login novamente.")