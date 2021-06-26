# Importando uma função específica de um módulo e atribuindo um alias ao módulo
from pizza import make_pizza as mp

mp(16,'pepperoni')

# A instrução import no exemplo renomeia a função make_pizza() para mp()
# nesse programa. Sempre que quiser chamar make_pizza(), você pode
# simplesmente escrever mp() em seu lugar, e Python executará o código de
# make_pizza(), ao mesmo tempo que evitará confusão com outra função
# make_pizza() que você possa ter escrito nesse arquivo de programa.

# A melhor abordagem é importar a função ou as funções que você
# quiser ou importar o módulo todo e usar a notação de ponto. Isso
# resulta em um código claro, mais fácil de ler e de entender. Incluí esta
# seção para que você possa reconhecer instruções import como esta
# quando as vir no código de outras pessoas: 
# from nome_do_módulo import *