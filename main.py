import trv
import random

print("key ______ -> updates key")
print("cypher ______ -> returns cyphered")
print("decypher ______ -> returns decyphered")
print("quit -> quits program")


def change_key(new_key):
	# change the key and print error messages
	global key
	try:
		new_key = int(new_key)
	except ValueError:
		print("new key must be an int:")
	key = new_key
	print("your key: " + str(key))

change_key(random.randint(int("1" * 12), int("9" * 12)))

while True:
	print()
	command = input("$ ")
	if len(command.split()) >= 1:
		if command.split()[0] == "cypher":
			command = command.replace("cypher ", "")
			tmp = trv.cypher(key, command)
			print(tmp)
			tmp = ""
		elif command.split()[0] == "decypher":
			command = command.replace("decypher ", "")
			tmp = trv.decypher(key, command)
			print(tmp)
			tmp = ""
		elif command.split()[0] == "key":
			command = command.replace("key ", "")
			change_key(command)
		elif command == "quit":
			break
			