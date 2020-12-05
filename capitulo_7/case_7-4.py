# 7.4 Ingredientes para uma pizza
prompt = "Escreva o nome dos ingredientes que você deseja na sua pizza. "
prompt += "\n(Digite 'quit' para sair.) "

# Recebe vazio para entrar no laço while
ingrediente = ""

# Enquanto nao tiver digitado 'quit'
while ingrediente != 'quit':
    # printa o prompt que vira entrada para ingrediente
    ingrediente = input(prompt)
    # se o usuario nao queiser sair, retorna mensagem com o ingrediente
    if ingrediente != 'quit':
        print("Irei adicionar " + ingrediente.title() + " na sua pizza.")
