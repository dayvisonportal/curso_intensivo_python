# 3.8 Conhecendo o mundo
locations_list = ['Location 4','Location 1', 'Location 3', 'Location 2', 'Location 5']

print("\nLista original: " + str(locations_list))

print("\nLista em ordem alfabetica: " + str(sorted(locations_list)))

print("\nLista original novamente: " + str(locations_list))

locations_list.reverse()
print("\nLista original reordenada: " + str(locations_list))

locations_list.reverse()
print("\nLista original novamente: " + str(locations_list))

locations_list.sort()
print("\nLista original reordenada: " + str(locations_list))

locations_list.sort(reverse=True)
print("\nLista original inversamente reordenada: " + str(locations_list))

