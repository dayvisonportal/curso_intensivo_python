# 6.10 Números favoritos
favorite_numbers = {
    'pessoa a':[10,11], 'pessoa b':[20,21]
    , 'pessoa x':[15,16], 'pessoa y':[17,18]
}

# items(), devolve lista de pares chave-valor
for key, favorite_number in favorite_numbers.items(): 
    print("Os números favoritos da " 
        + key.title()
        + " são "
        + str(favorite_number)
        + "."
    )