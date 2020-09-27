# 4.3 Contando até vinte
for value in range(1,21):
    print(value)

# 4.4 Um milhão
values = []
for value in range(1,1000001):
    values.append(value)

#print(values)    

# 4.5 Somando um milhão
print("\n")
print(min(values))
print(max(values))
print(sum(values))

# 4.6 Números ímpares
print("\n")

for value in range(1,21):
    odd_numbers = list(range(1,21,2))
print(odd_numbers)

# 4.7 Múltiplos de Três
print("\n")
for value in range(1,31):
    print(3 * value)

# 4.8 Cubo
print("\n")
for value in range(1,11):
    print(value**3)

# Comprehension de cubos
print("\n")
comprehension = [value ** 3 for value in range(1,11)]
print(comprehension)


