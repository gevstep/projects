# Task 1
user_string = input("Enter your text: ")
user_string = bool(user_string)
if  user_string == False:
	#print("Your input is empty")
else:
	print("You enter text: ", user_string)
# Task 2
temperature = int(input("Enter temperature: "))
print(temperature * 1.5, "Farenheit")
# Task 3
d1 = int(input("Enter first number: "))
d2 = int(input("Enter second number: "))
if d1 == 1 or d1 == 2 or d1 == 3 or d1 == 4 or d1 == 5 or d1 == 6:
	if d1 + d2 == 7 or d1 + d2 == 11:
		print("WINNER!!!")
	elif d1 + d2 == 2 or d1 + d2 == 3 or d1 + d2 ==12:
		print("LOSER!!!")
	else:
		print("..............")
else:
	print("You enter not dice number")