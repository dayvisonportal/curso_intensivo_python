# Introdução aos laços while
# Laço while em ação

current_number_a = 1

while current_number_a <= 5:
    print(current_number_a)
    current_number_a += 1

print("\n")

# Usnado continue em um laço

current_number_b = 0

while current_number_b < 10:
    current_number_b += 1
    # Se o módulo for 0 (o que significa que current_number é divisível por 2),
    # a instrução continue diz a Python para ignorar o restante do laço e
    # voltar ao início.
    # Regra de divisibilidade, todo número dividido por 2 é par.
    if current_number_b % 2 == 0:
        continue
    print(current_number_b)
