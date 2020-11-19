# Os dez primeiros quadrados perfeitos em uma lista
squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)

print(squares)    

# Mesmo código, mais conciso
squares = []
for value in range(1,16):
    squares.append(value**2)

print(squares)


# List comprehension
squares = [value**2 for value in range(1,21)]
print(squares)


#digits = [1,2,3,4,5,6,7,8,9,0]

#min(digits)
#print(min(digits))
#print(max(digits))
#print(sum(digits))