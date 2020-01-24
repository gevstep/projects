bank_account = 5000
user_inputed_item_price = int(input('Enter price of item what you want to buy: '))
if bank_account >= user_inputed_item_price:
	print("You can buy this item: ")
elif input("You don't have enough money, do you want a loan? y/n: ") == "y" and bank_account + int(input("How much do you want? ")) >= user_inputed_item_price:
		print("Now you can buy this item: ")
else:
	print("You can't buy this item")