# Percorrendo todos os pares chave-valor com um laço
user_0 = {
    'username':'efermi', 'first':'enrico', 'last':'fermi',
}

for key, value in user_0.items(): # items(), devolve uma lista de pares chave-valor
    print("\nKey: " + key)
    print("Value: " + value)