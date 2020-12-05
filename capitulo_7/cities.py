# Usando break para sair de um laço (tanto while quanto for)

prompt = "\nPlease enter the name of a vity have visited."
prompt += "\n(Enter 'quit' when you are finished.) "

# Um laço que comece com while True executará
# indefinidamente, a menos que alcance uma instrução break

while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print("I'd love to go to " + city.title() + "!")
