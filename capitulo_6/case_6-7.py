# 6.7 Pessoas
pessoas_0 = {
    'first_name':'dayvison','last_name':'portal'
    , 'age':28, 'city':'belem'
}

pessoas_1 = {
    'first_name':'daltro','last_name':'pina'
    , 'age':27, 'city':'belem'
}

pessoas_2 = {
    'first_name':'flavia','last_name':'dahas'
    , 'age':27, 'city':'belem'
}

people = []

people.append(pessoas_0)
people.append(pessoas_1)
people.append(pessoas_2)
print(people)
 
# Dicionarios dentro de uma lista para expor suas informações
for person in people:
    print(person['first_name'].title()
    + " " + person['last_name'].title()
    + " tem " + str(person['age'])
    + " anos e mora em " + person['city'].title()
    + "."
    )
    