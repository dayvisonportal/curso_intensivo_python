# 8.12 Sanduíches
def make_sandwich(*molhos):
    """Apresenta o sanduíche que estamos prestes a preparar"""
    print("Preparando o sanduíche com os molhos de: ")
    for molho in molhos:
        print("- " + molho.title())


make_sandwich('barbecue')
make_sandwich('maionese', 'agridoce', 'parmesao')
make_sandwich('molho a', 'molho b', 'molho c', 'molho d', 'molho e')
