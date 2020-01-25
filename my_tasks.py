# Task 41
first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))
third_number = int(input("Enter third number: "))
print(first_number, second_number, third_number)
t = False
if third_number == first_number + second_number:
	t = True
	print(t)
else:
	print(t)
# Task 42
first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))
third_number = int(input("Enter third number: " ))
t = False
if first_number == second_number or first_number == third_number:
	t =True
	print(t)
else:
	print(t)
# Task 43
number_inputed = int(input("Enter three digit number: "))
k = 500
number = number_inputed % 1000
first = number_inputed % 10
second = number_inputed % 100
second = int(second / 10)
third = int(number / 100)

if number_inputed > k:
	x = (first + second +third)/ (first / second / third)
	print(x)
else:
	y = first / second / third
	print(y) 
 	
# Task 44
user_number = int(input("Enter three digit number: "))
first = int(user_number / 100)
second = int(user_number % 100 / 10)
third = int(user_number % 10)
if first > second and first > third:
	print(first)
elif second > first and second > third:
	print(second)
elif third > first and third > second:
	print(third)
else:
	print("All entered numbers is equal: ")
# Task 45
user_number = int(input("Enter three digit number: "))
first = int(user_number / 100)
second = int(user_number % 100 / 10)
third = int(user_number % 10)
if first < second and first < third:
	print(first)
elif second < first and second < third:
	print(second)
elif third < first and third < second:
	print(third)
else:
	print("All entered numbers is equal: ")
# Task 46
user_number = int(input("Enter three digit number: "))
first = int(user_number / 100)
second = int(user_number % 100 / 10)
third = int(user_number % 10)
if third > second:
	print((first + second + third)*user_number)
else:
	print(user_number)
# Task 47
user_number = int(input("Enter three digit number: "))
first = int(user_number / 100)
second = int(user_number % 100 / 10)
third = int(user_number % 10)
x = 300
if user_number > x:
	print(second * third)
else:
	print(first * third)
# Task 48
user_number = int(input("Enter three digit number: "))
first = int(user_number / 100)
second = int(user_number % 100 / 10)
third = int(user_number % 10)
f = "a"
if first + second < 5:
	print(f)
else:
	f = "b"
	print(f)
# Task 49
user_number = int(input("Enter three digit number: "))
first = int(user_number / 100)
second = int(user_number % 100 / 10)
third = int(user_number % 10)
if first > second and first > third and second > third:
	print(third, second, first)
elif first > second and first > third and third > second:
	print(second, third, first)
elif second > first and second > third and first > third:
	print(third, first, second)
elif second > first and second > third and third > first:
	print(first, third, second)
elif third > first and third > second and second > first:
	print(first, second, third)
elif third > first and third > second and first > second:
	print(second, first, third)
elif first > second and second == third:
	print(second, third, first)
elif second > first and first == third:
	print(first, third, second)
elif third > first and first == second:
	print(first, second, third)
else:
	print("All entered numbers is equal:", user_number)

	