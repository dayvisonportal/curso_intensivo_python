# 5.2 Mais testes condicionais
test_1 = "one more test"

if test_1 == "one more test":
    print("This " + test_1 + " is True.")
else:
    print('This ' + test_1 + ' is False.')


animal = 'Cat'

if animal.lower() == 'cat':
    print("\nIndeed a " + animal.title() + " is a " + animal + ".")
else:
    print("\n" + str(False))


friend_lists = [
    "Friend A", "Friend B", "Friend C"
]
if "Friend X" not in friend_lists:
    print("\nFriend X is not my friend.")