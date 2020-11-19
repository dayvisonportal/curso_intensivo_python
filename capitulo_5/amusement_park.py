# Sintaxe if-elif-else
age = 12

if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $5.")
else:
    print("Your admission cost is $10.")

print("\n")    

if age < 4: 
    price = 0
    print("Your admission cost is $" + str(price) + ".")
elif age < 18:
    price = 5
    print("Your admission cost is $" + str(price) + ".")
elif age < 65:
    price = 10
    print("Your admission cost is $" + str(price) + ".")
elif age >= 65:
    price = 5
    print("Your admission cost is $" + str(price) + ".")
#else:
    #price = 5
    #print("Your admission cost is $" + str(price) + ".")    