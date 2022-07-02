import random
import pyperclip

length = 8
length = int(input("Enter password length: "))

def generate():
	pass1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
	            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
	            'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
	            'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
	            'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 
	            'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', 
	            '9', '0', ' ', '!', '@', '#', '$', '%', '^', '&', 
	            '*', '(', ')']

	password = ""
	for x in range(length):
		password = password + random.choice(pass1)
	print(password)
	pyperclip.copy(password)
	print("Password copied to clipboard.")



if length == 0 :
	print("Enter a valid length")
else:
	generate()