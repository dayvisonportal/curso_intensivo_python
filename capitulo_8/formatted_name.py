# Valores de Retorno
# Devolvendo um valor simples
# Deixando um argumento opcional
def get_formatted_name(first_name, last_name, middle_name=''):
    # Python interpreta strings não vazias como True
    # Ou seja, entra no if se o parametro for preenchido (middle_name)
    """Devolve um nome completo formatado de mogo elegante."""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
        return full_name.title()
    else:
        full_name = first_name + ' ' + last_name
        return full_name.title()


musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)
