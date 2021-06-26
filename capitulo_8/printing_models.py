from printing_functions import print_models, show_completed_models

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

f_unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
f_completed_models = []

print_models(f_unprinted_designs, f_completed_models)
show_completed_models(f_completed_models)
