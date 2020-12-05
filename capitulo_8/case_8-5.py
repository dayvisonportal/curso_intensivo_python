# 8.5 Cidades
def describe_city(cidade, pais='Islandia'):
    print(
        cidade.title()
        + " está localizado na(o) "
        + pais.title()
        + "."
    )


describe_city('reykjavik')
describe_city('belem', 'brasil')
describe_city('barcarena', 'brasil')
