# 6.9 Lugares favoritos

favorite_places = { # Questionario
    #'Pessoa N': [Deu duas respostas]
    'pessoa a':['cidade a', 'cidade x'],
    'pessoa b':['cidade b', 'cidade y'],
    'pessoa c':['cidade c', 'cidade z'],
}

# Para <chave>, <valor> dentro do dicionário
for person, favorite_place in favorite_places.items():
    # Retornar a <chave>
    print("Os lugares favoritos de " + person.title()
    # Retornar o <valor> contido na <posição 0 da lista>
    + " são " + favorite_place[0].title() + " e " 
    # Retornar o <valor> contido na <posição 1 da lista>
    + favorite_place[1].title() + "."
    )
