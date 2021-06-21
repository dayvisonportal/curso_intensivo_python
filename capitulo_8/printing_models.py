# Modificando uma lista em uma função

# Começa com alguns designs que devem ser impressos
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

# Simula a impressão de cada design, até que não haja mais nenhum
# Transfere cada design para completed_models após a impressão
while unprinted_designs:
    current_design = unprinted_designs.pop()
    # Simula a criação de uma impressão 3D a aprtir do deisgn
    print("Printing model: " + current_design)
    completed_models.append(current_design)

# Exibe todos os modelos finalizados
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)

print("=========================================================")

# Criando funções para deixar o código mais eficiente


def print_models(f_unprinted_designs, f_completed_models):
    """Simula a impressão de cada deisgn, até que não haja mais nenhum."""
    """Transfere cada design para completed_models após a impressão."""
    while f_unprinted_designs:
        f_current_design = f_unprinted_designs.pop()
        # Simula a criação de uma imporessão 3D a partir do design
        print("Printing model: " + f_current_design)
        f_completed_models.append(f_current_design)


def show_completed_models(f_completed_models):
    """Mostra todos os modelos impressos."""
    print("\nThe following models have been printed:")
    for f_completed_model in f_completed_models:
        print(f_completed_model)


f_unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
f_completed_models = []

print_models(f_unprinted_designs, f_completed_models)
show_completed_models(f_completed_models)
