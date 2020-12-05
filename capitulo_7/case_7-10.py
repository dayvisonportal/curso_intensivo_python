# 7.10 Férias dos sonhos
responses = {}

active = True

while active:
    name = input("\nDigite o seu nome: ")
    response = input(
        "\nSe pudesse visitar um lugar do mundo, para onde você iria? ")
    responses[name] = response
    repeat = input("Outra pessoa irá responder? (sim/ nao) ")
    if repeat == 'nao':
        active = False
        print("\n--- Enquete dos sonhos ---")
        for name, response in responses.items():
            print(name.title() + " gostaria de ir para " + response.title() + ".")
