# Capitulo 1 - A Teoria da Demanda e da Oferta

def elasticidade_preco_demanda(aumento_preco_produto, demanda_produto):
    # print("\nPreço do produto aumenta em " + str(aumento_preco_prod) + "%.")
    # print("Quantiadde da demanda cai em " + str(demanda_prod) + "%.")
    epd = demanda_produto/aumento_preco_produto
    epd = abs(round(epd, 2))  # Apenas 2 casas decimais
    if epd > 1:
        print("\nPara cada aumento de preço de 1% ocorre uma QUEDA de "
              + str(epd) + "% na quantidade demandada. Desta forma, a"
              + " demanda é Elástica, onde o gasto do consumidor e a receita"
              + " de vendas diminui se o preço subir.")
    # Se o preço subir, haverá uma queda percentual maior ainda na quantidade
    # comprada. Os gastos do consumidor e a receita das vendas cairão. Para os
    # consumidores esse produto provavelmente não é importante ou tem
    # substitutos próximos pois há uma forte redução de sua demanda devido ao
    # aumento de preço. A demanda é dita Elástica.
    elif epd < 1:
        print("\nPara cada aumento de preço de 1% ocorre uma REDUÇÃO de "
              + str(epd) + "% na quantidade consumida. Portanto, a demanda é"
              + " Inelástica, no qual o gasto do consumidor e a receita de"
              + " vendas aumentam se o preço aumentar.")
    # Provavelmente o consumidor tem poucas oçpões de substituir este bem;
    # continua comprando quase a mesma quantidade, apesar da subida do preço.
    elif epd == 1:
        print("\nPara cada aumento de preço de 1% ocorrerá uma REDUÇÃO de "
              + str(epd) + "% na quantidade comprada. Por serem constantes, a "
              + "elasticidade-preço é dita Unitária, onde a decisão de "
              + "aumentar os preços não irá modificar o gasto do consumidor"
              + "  nem a receita de vendas.")
    # O consumidor reduz as quantidads na mesma proporção da subida dos preços.
    else:
        False


def elasticidade_renda_demanda(renda_real, qtd_adquirida_produto):
    erd = qtd_adquirida_produto/renda_real
    erd = round(erd, 2)
    print("\nPara o indivíduo em questão: ")
    if erd < 0:
        print("- O bem ou serviço é considerado Inferior, pois a cada 1% no"
              + " aumento de sua renda ocorre uma QUEDA de "
              + str(abs(erd)) + "% na quantidade demandada.")
    elif (erd < 1):
        print("- O bem ou serviço é considerado Essencial, pois a cada 1% no"
              + " aumento de sua renda há um AUMENTO de "
              + str(abs(erd)) + "% na quantidade demandada.")
    elif erd > 1:
        print("- O bem ou serviço é considerado Supérfluo, pois a cada 1% no"
              + " aumento de sua renda há um AUMENTO de "
              + str(abs(erd)) + "% na quantidade demandada.")
    else:
        False


def elasticidade_preco_oferta(preco_mercadoria, quantidade_ofertada):
    epo = quantidade_ofertada/preco_mercadoria
    epo = round(epo, 2)
    if epo > 1:
        print("\nPara cada aumento de preço de 1% ocorrerá uma elevação "
              + "na quantidade ofertada de "
              + str(abs(epo)) + ". Isso mostra que "
              + "a estrutura produtiva desta mercadoria tem poucas restrições"
              + " e é capaz de responder prontamente ao estímulo de preços, "
              + "portanto, trata-se de uma oferta Elástica. ")
    elif epo < 1:
        print("\nPara cada aumento de preço de 1% ocorrerá uma elevação "
              + "na quantidade ofertada de apenas "
              + str(abs(epo)) + ". A estrutura produtiva responde com "
              + "dificuldade ao estímulo de preços.")
    else:
        False


prompt = int(input(
    "\nDigite (1) Elasticidade-preço Demanda | (2) Elasticidade-renda Demanda | (3) Elasticidade-preço Oferta: "))

if prompt == 1:
    aumento_preco_prod = float(
        input("O preço do produto aumentou em quantos %? "))
    demanda_prod = float(input("A demanda do produto caiu em quantos %? "))
    # Chamada da função passando os 2 parâmetros
    elasticidade_preco_demanda(aumento_preco_prod, demanda_prod)
elif prompt == 2:
    renda = float(input("A renda real da família aumentou em quantos %? "))
    qtd_adq_prod = float(
        input("A quantidade adquirida do produto aumentou em quantos %? "))
    # Chamada da função passando os 2 parâmetros
    elasticidade_renda_demanda(renda, qtd_adq_prod)
elif prompt == 3:
    preco_merc = float(input("O preço da mercadoria aumentou em quantos %? "))
    qtd_ofertada = float(
        input("A quantidade ofertada aumentou em quantos %? "))
    # Chamada da função passando os 2 parâmetros
    elasticidade_preco_oferta(preco_merc, qtd_ofertada)
