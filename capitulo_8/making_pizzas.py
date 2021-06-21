# Importando um módulo completo
import pizza

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# Essa primeira abordagem à importação, em que simplesmente
# escrevemos import seguido do nome do módulo, deixa todas as funções
# do módulo disponíveis ao seu programa. Se você usar esse tipo de
# instrução import para importar um módulo completo chamado
# nome_do_módulo.py, todas as funções do módulo estarão disponíveis por
# meio da sintaxe a seguir: nome_do_módulo.nome_da_função()
