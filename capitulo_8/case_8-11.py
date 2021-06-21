# 8.10 Grandes Mágicos
def make_great(magicians, great_magicians):
    """Modifica o mágico adicionando a expressão Grande ao nome."""
    # Enquanto houver mágicos na lista
    while magicians:
        # Mágico da lista vai para variável do mágico atual
        current_magician = magicians.pop()
        # Processo de MakingGreat
        # Lista do great_magicians recebe o mágico atual
        print("Making Great: " + current_magician.title() + "!")
        great_magicians.append("Great " + current_magician.title())


def show_magicians(great_magicians):
    """Devolve o nome dos mágicos."""
    for great_magician in great_magicians:
        print(great_magician.title())


# Declara as listas a serem utilizadas nas funções
magicians = ['green magician', 'yellow magician', 'red magician']
great_magicians = []

# Cópia da lista modificada
print("\n### Cópia da lista modificada ###")
make_great(magicians[:], great_magicians)
show_magicians(great_magicians)

# Lista Original
print("\n### Lista original ###")
show_magicians(magicians)
