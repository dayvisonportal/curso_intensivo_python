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