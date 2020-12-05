# Como a função input() trabalha
# Faz uma pausa em seu programa e espera o usuário fornecer um dado.
# message = input("Tell me something, and I will repeat it back to you: ")
# print(message)

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

# É declarado uma variável com valor para que na
# primeira iteração do while, exista algo a ser avaliado
message = ""

while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)
