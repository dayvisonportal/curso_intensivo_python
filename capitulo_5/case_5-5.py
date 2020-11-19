# 5.5 Cores de alienígenas #3
alien_color = [
    'green','yellow', 'red'
]

alien = 'green'
if alien in alien_color:
    score = 5
    print("Jogador 1 acabou de ganhar " + str(score) + " pontos.")
elif alien in alien_color:
    score = 10
    print("Jogador 1 acabou de ganhar " + str(score) + " pontos.")
elif alien in alien_color:
    score = 15
    print("Jogador 1 acabou de ganhar " + str(score) + " pontos.")

alien = 'yellow'
if alien not in alien_color:
    score = 5
    print("Jogador 1 acabou de ganhar " + str(score) + " pontos.")
elif alien in alien_color:
    score = 10
    print("Jogador 1 acabou de ganhar " + str(score) + " pontos.")
elif alien in alien_color:
    score = 15
    print("Jogador 1 acabou de ganhar " + str(score) + " pontos.")

alien = 'red'
if alien not in alien_color:
    score = 5
    print("Jogador 1 acabou de ganhar " + str(score) + " pontos.")
elif alien not in alien_color:
    score = 10
    print("Jogador 1 acabou de ganhar " + str(score) + " pontos.")
elif alien in alien_color:
    score = 15
    print("Jogador 1 acabou de ganhar " + str(score) + " pontos.")        