# Passando um número arbitrário de argumentos
def make_pizza(size, *toppings):
    """Apresenta a pizza que estamos prestes a preparar."""
    print("\nMaking a " + str(size) +
          "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)


# make_pizza(16, 'peperoni')
# make_pizza(12, 'mushrooms', 'green peppers', 'exra cheese')

# O asterisco no nome do parâmetro *toppings diz a Python para
# criar uma tupla vazia chamada toppings e reunir os valores recebidos
# nessa tupla. A instrução print no corpo da função gera uma saída que
# mostra que Python é capaz de tratar uma chamada de função com um valor
# e outra chamada com três valores. As chamadas são tratadas de modo
# semelhante.

# >> Misturando argumentos posicionais e abritrários << #
# Se quiser que uma função aceite vários tipos de argumentos, o
# parâmetro que aceita um número arbitrário de argumentos deve ser
# colocado por último na definição da função. Python faz a
# correspondência de argumentos posicionais e nomeados antes, e depois
# agrupa qualquer argumento remanescente no último parâmetro.
