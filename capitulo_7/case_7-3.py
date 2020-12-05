# 7.3 Multiplos de Dez
prompt = input("Me diga um número e direi se é ou não múltiplo de dez: ")
print(prompt)

number = int(prompt)

# Se o resto da divisão for igual a 0, então é multiplo
if (number % 10 == 0):
    print("O número " + str(number) + " é múltiplo de 10.")
else:
    print("O número " + str(number) + " não é múltiplo de 10.")
