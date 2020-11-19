# 6.11 Cidades
cities = {
    'belem': {'country':'brasil','population':'1492745','fact':'top 12 mais populoso do Brasil', },
    'barcarena': {'country':'brasil','population':'124680','fact':'maior porto do Para', },
    'ananindeua': {'country':'brasil','population':'525566','fact':'conurbada com Belem', },
}

# Jamais esquecer que um dicionario para um laço for precisa do .items()
for city, city_info in cities.items(): 
    print("\n" + city.title() + ":")

    informacao_1 = city_info['country']
    informacao_2 = city_info['population']
    informacao_3 = city_info['fact'] 

    print("\tInformação 01: Pertence ao " + informacao_1.title() + ";")
    print("\tInformação 02: População de " + informacao_2.title() + " habitantes;")
    print("\tInformação 03: " + informacao_3.title() + ";")

