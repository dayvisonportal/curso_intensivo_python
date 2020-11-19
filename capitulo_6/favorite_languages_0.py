# Um dicionário de objetos semelhantes
favorite_languages = {
    'jen':'python', 'sarah':'c'
    , 'edward':'ruby', 'phil':'python'
}

print("Sarah's favorite language is "
    + favorite_languages['sarah'].title()
    + ".\n"
)


# Percorrendo todos os pares chave-valor com um laço
for name, language in favorite_languages.items():
    print(name.title() 
    + "'s favorite language is " 
    + language.title()
    + "."
    )


print("\n")
# Percorrendo todas as chaves de um dicionário com um laço
for name in favorite_languages.keys(): # .keys() explicito
    print(name.title())

for name in favorite_languages:        # .keys() implicito
    print(name.title())

print("\n")
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())
    if name in friends:
        print(" Hi "
        + name.title()
        + ", I see your favorite language is "
        + favorite_languages[name].title()
        + "!"
        )

if 'erin' not in favorite_languages.keys():
    print("\nErin, please take our poll!")

print("\n")
# Percorrendo as chaves de um dicionário em ordem usando um laço
for name in sorted(favorite_languages.keys())    :
    print(name.title()
    + ", thank you for taking the poll."
    )

# Percorrendo todos os valores de um dicionário com um laço    
print("\nThe following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

print("\nThe following languages have been mentioned:")
for language in set(favorite_languages.values()): # set() retorna valores únicos (distinct no sql)
    print(language.title())    