# Escrevendo prompts claros
prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is yout first name? "
print(prompt)


name = input("Please enter your name: ")
print("\nHello, " + name.title() + "!")
