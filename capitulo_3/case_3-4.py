# Lista de convidados
guest_list = ['Convidado A','Convidado B','Convidado C']
print("Olá, gostaria de jantar comigo esta noite, " + guest_list[0] + "?")
print("Olá, gostaria de jantar comigo esta noite, " + guest_list[1] + "?")
print("Olá, gostaria de jantar comigo esta noite, " + guest_list[2] + "?")

# Alterando a lista de convidados
print("\nO " + guest_list[1] + " não poderá comparecer ao jantar esta noite.\n")
del guest_list[1]

guest_list.insert(1,"Convidada D")
print("Olá, gostaria de jantar comigo esta noite, " + guest_list[0] + "?")
print("Olá, gostaria de jantar comigo esta noite, " + guest_list[1] + "?")
print("Olá, gostaria de jantar comigo esta noite, " + guest_list[2] + "?")

# Mais convidados
print("\nAmigos, encontrei uma mesa maior, vou chamar mais três pessoas!\n")

guest_list.insert(0, "Convidado E")
guest_list.insert(2, "Convidado F")
guest_list.append("Convidado G")

print("Olá, gostaria de jantar comigo esta noite, " + guest_list[0] + "?")
print("Olá, gostaria de jantar comigo esta noite, " + guest_list[1] + "?")
print("Olá, gostaria de jantar comigo esta noite, " + guest_list[2] + "?")
print("Olá, gostaria de jantar comigo esta noite, " + guest_list[3] + "?")
print("Olá, gostaria de jantar comigo esta noite, " + guest_list[4] + "?")
print("Olá, gostaria de jantar comigo esta noite, " + guest_list[5] + "?")

# Reduzindo a lista de convidados
print("\nDesculpa pessoal, a mesa não vai chegar a tempo, então só irei chamar duas pessoas.\n")

guest_absent = []
guest_absent.append(guest_list.pop(0))
guest_absent.append(guest_list.pop(0))
guest_absent.append(guest_list.pop(0))
guest_absent.append(guest_list.pop(0))

print("Sinto muito, " + guest_absent[0] + "! Não poderei te convidar para o jantar.")
print("Sinto muito, " + guest_absent[1] + "! Não poderei te convidar para o jantar.")
print("Sinto muito, " + guest_absent[2] + "! Não poderei te convidar para o jantar.")
print("Sinto muito, " + guest_absent[3] + "! Não poderei te convidar para o jantar.\n")
print(guest_absent)

print("\nOlá, gostaria de jantar comigo esta noite, " + guest_list[0] + "?")
print("Olá, gostaria de jantar comigo esta noite, " + guest_list[1] + "?\n")

del guest_list[0]
del guest_list[0]
print(guest_list)