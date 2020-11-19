# 6.8 Animais de Estimação
cachorros = {'tipo':'cachorro','dono':'dayvison'}
gatos = {'tipo':'gato','dono':'flavia'}
quatis = {'tipo':'quati','dono':'victor'}

pets = []
pets.append(cachorros)
pets.append(gatos)
pets.append(quatis)

for pet in pets:
    print("O " + pet['tipo'] + " é um animal de estimação e o(a) "
    + pet['dono'].title() + " é dono de um."
    )