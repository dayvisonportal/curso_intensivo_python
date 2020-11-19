# 6.5 Rios
rios = {
    'nilo':'egito'
    , 'rio x':'pais x'
    , 'rio y':'pais y'
}

# Exibir a frase
for rio, pais in rios.items():
    print(
        "O " + rio + " corre pelo pais " + pais + "."
    )

print("\n")    

# Exibir somente as chaves do dicionario
for key in rios.keys():
    print(key)

print("\n")

# Exibir somente os valores do dicionario
for valor in rios.values():
    print(valor)

