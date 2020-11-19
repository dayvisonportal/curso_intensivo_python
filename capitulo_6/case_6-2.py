# 6.2 Números favoritos
favorite_numbers = {
    'pessoa a':10, 'pessoa b':20
    , 'pessoa x':15, 'pessoa y':17
}

# items(), devolve lista de pares chave-valor
for key, favorite_number in favorite_numbers.items(): 
    print("O número favorito da " 
        + key.title()
        + " é "
        + str(favorite_number)
        + "."
    )