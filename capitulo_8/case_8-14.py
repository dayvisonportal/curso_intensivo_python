def make_car(fabricante, modelo, cor, **opcional):
    """Constrói um dicionário contendo tudo que sabeos sobre um usuário."""
    car = {}
    car['fabricante'] = fabricante
    car['modelo'] = modelo
    car['cor'] = cor
    for key, value in opcional.items():
        car[key] = value
        return car


user_car = make_car(
    'subaru', 'outback', 'blue', pelicula=True)
print(user_car)
