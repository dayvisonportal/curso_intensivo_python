# Passando argumentos
def describe_pet(animal_type, pet_name):
    """Exibe informações sobre um animal de estimação."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


# Argumentos posicionais
describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')

# Argumentos nomeados
describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(animal_type='dog', pet_name='willie')

# Valores default


def describe_pet_default(pet_name, animal_type='dog'):
    """Exibe informações sobre um animal de estimação."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


describe_pet_default(pet_name='willie')
describe_pet_default(pet_name='willie', animal_type='harry')

# Chamadas de função equivalentes

# Um cachorro chamado Willie
describe_pet_default('willie')
describe_pet_default(pet_name='willie')

# Um hamster chamado Harry
describe_pet_default('harry', 'hamster')
describe_pet_default(pet_name='harry', animal_type='hamster')
describe_pet_default(animal_type='hamster', pet_name='harry')
