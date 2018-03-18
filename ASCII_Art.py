import pyfiglet

def start():
	result = input("Type a message: ")
	return print(pyfiglet.figlet_format(result))

start()