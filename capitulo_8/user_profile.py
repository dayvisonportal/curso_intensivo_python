# Usando argumentos nomeados arbitrários
def build_profile(first, last, **user_info):
    """Constrói um dicionário contendo tudo que sabeos sobre um usuário."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
        return profile


user_profile = build_profile(
    'albert', 'einstein', location='princeton', field='physics')
print(user_profile)

# Às vezes, você vai querer aceitar um número arbitrário de argumentos,
# mas não saberá com antecedência qual tipo de informação será passado
# para a função. Nesse caso, podemos escrever funções que aceitem
# tantos pares chave-valor quantos forem fornecidos pela instrução que
# faz a chamada.
