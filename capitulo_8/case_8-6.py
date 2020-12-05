# 8.6 Nomes de cidade
def city_country(cidade, pais):
    """Devolve o nome da cidade com seu país."""
    cidade_pais = cidade + ', ' + pais
    return cidade_pais.title()


nomes_da_cidade = city_country('santiago', 'chile')
print(nomes_da_cidade)

nomes_da_cidade = city_country(cidade='belem', pais='brasil')
print(nomes_da_cidade)

nomes_da_cidade = city_country('barcarena', pais='brasil')
print(nomes_da_cidade)
