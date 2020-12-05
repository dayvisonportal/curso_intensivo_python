# 8.4 Camisetas grandes
def make_shirt(tamanho='G', estampa='Eu amo Python'):
    print("O tamanho da camisa é "
          + tamanho
          + " e a frase estampada é "
          + estampa + "."
          )


# Chamando função com argumentos default
make_shirt()

# Chamando função com argumentos nomeados
make_shirt(tamanho='P', estampa='GoLive SGU')
