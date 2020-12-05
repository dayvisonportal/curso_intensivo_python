# Como mostrar cada item de uma lista (Range)

# Cria uma lista que se extende do 0 até o 4 (5 valores)
# lista = range(5)
# print(lista)
# Para cada índice da lista (5 valores), retornar cada valor
# for numero in lista:
# print(numero)

# 7.3 Multiplos de Dez (Aprimorado)
multiplo = input("\nQual número vamos testar se é múltiplo? ")

prompt = "Me diga mais dois números e direi quais, entre o intervalo, "
prompt += "são múltiplos de " + multiplo + "."
print(prompt)

prompt_a = input("Qual o primeiro número? ")
number_a = int(prompt_a)

prompt_b = input("Qual o segundo número? ")
number_b = int(prompt_b)

numbers = range(number_a, (number_b+1))
# for i in numbers:
# print(i)

# Se o resto da divisão for igual a 0, então é multiplo
print("\n")
for i in numbers:
    # if (i % int(multiplo) == 0) and (i % 5 == 0):
    if (i % int(multiplo) == 0):
        print("O número " + str(i) + " é múltiplo de " + multiplo + ".")
    # else:
    #    print("O número " + str(i) + " não é múltiplo de " + multiplo + ".")
