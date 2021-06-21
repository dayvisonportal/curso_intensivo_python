def preco_hora_regular(salario, carga_hora_semanal=44):
    """Faz o cálculo da jornada de trabalho regular"""
    # 44 horas x 5 semanas = 220 horas mensais
    carga_hora_semanal = carga_hora_semanal * 5
    if prompt == 2:
        valor_hora_trabalho = round(salario_bruto / carga_hora_semanal, 2)
        print("1 hora equivale à R$" +
              str(valor_hora_trabalho).replace(".", ",") + " reais.")
        custo_cem = round(100 / valor_hora_trabalho)
        print("Para ganhar 100 reais é preciso trabalhar " +
              str(custo_cem) + " horas.")
    else:
        valor_hora_trabalho = round(salario_liquido / carga_hora_semanal, 2)
        print("1 hora equivale à R$" +
              str(valor_hora_trabalho).replace(".", ",") + " reais.")
        custo_cem = round(100 / valor_hora_trabalho)
        print("Para ganhar 100 reais é preciso trabalhar " +
              str(custo_cem) + " horas.")


salario_bruto = 0.0
salario_liquido = 0.0
valor_hora_trabalho = 0.0
custo_cem = 0.0

prompt = int(
    input("\nDigite (1) - Salário Líquido ou Digite (2) - Salário Bruto: "))
if prompt == 2:
    salario_bruto = 3649.72
    preco_hora_regular(salario=salario_bruto)
if prompt == 1:
    salario_liquido = float(input("Qual foi o salário líquido no mês? "))
    preco_hora_regular(salario=salario_liquido)

# Melhorar código
# Opcao para colocar carga horaria, se ficar em branco, considerar default
# if tem que ficar dentro de uma funcao
# objetivo é chamar tanto o custo_cem qt a funcao if em outro .py e funcionar hehe
