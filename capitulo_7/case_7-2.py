# 7.2 Lugares em um restaurante

# A resposta será um numero
prompt = input("\nQuantas pessoas estão em seu grupo para jantar? ")
qtd_pessoa = int(prompt)

if (qtd_pessoa > 8):
    print("Sinto muito, mas vocês precisarão esperar por uma mesa.")
else:
    print("Sua mesa está pronta!")
