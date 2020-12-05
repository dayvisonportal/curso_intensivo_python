# Operador de módulo

# Quando um número é divisível por outro, o resto é 0, portanto o
# operador de módulo sempre devolve 0 nesse caso.
# Podemos usar esse fato para determinar se um número é par ou ímpar:

prompt = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(prompt)

if number % 2 == 0:
    print("\nThe number " + str(number) + " is even.")
else:
    print("\nThe number " + str(number) + " is odd.")

# Números pares são sempre divisíveis por dois, portanto, se o módulo entre um
# número e dois for zero (nesse caso, if number % 2 == 0), o número será par.
# Caso contrário, será ímpar.
