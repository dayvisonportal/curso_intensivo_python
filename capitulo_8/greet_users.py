# Passando uma lista para uma função
def greet_users(names):
    """Exibe uma saudação simples a cada usuario da lista."""
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)


usernames = ['hanna', 'ty', 'margot']
greet_users(usernames)
