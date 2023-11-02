def introduction(n1, n2):
	return "Hello, my name is " + n1 + ". What is your name? Hello " + n1 + ", my name is " + n2 + ". Nice to meet you."

person1 = input("Give me a name: ")
person2 = input("Gave me another name: ")

print(introduction(person1, person2))