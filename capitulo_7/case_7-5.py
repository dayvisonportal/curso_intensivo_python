# 7.5 Ingressos para o cinema
prompt = "Bem vindo(a) ao cinema!"
prompt += "\nMe diga a sua idade e te direi o valor do ingresso. "

active = True

while True:
    idade = int(input(prompt))
    # idade = int(idade)
    if idade < 3:
        print("O seu ingresso é gratuito!")
        break
    elif idade <= 12:
        print("O seu custa 10 dólares!")
        break
    elif idade > 12:
        print("O seu custa 15 dólares!")
        break
    else:
        active = False
