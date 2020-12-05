# 8.3 Camiseta
def make_shirt(tamanho, estampa):
    print("O tamanho da camisa é "
          + tamanho
          + " e a frase estampada é "
          + estampa + "."
          )


# Chamando função com argumentos posicionados
make_shirt('M', 'GoLive SGU')

# Chamando função com argumentos nomeados
make_shirt(tamanho='M', estampa='GoLive SGU')
