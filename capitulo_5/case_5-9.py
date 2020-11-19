# 5.9 Sem usuários
users = []

if users:
    for user in users:
        if user == 'admin':
            print("Olá " + user.title() + ", gostaria de ver um relatório de status?")
        else:
            print("Olá " + user.title() + ", obrigado por fazer login novamente.")
else:
    print("Precisamos encontrar alguns usuários!")