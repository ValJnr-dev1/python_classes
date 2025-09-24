"""
#validation
balance = 20000
user_amount = input("Amount to withdraw:\n")
amount = int(user_amount)
if amount <=0:
	print("Invalid amount")
elif amount % 500 != 0:
	print("Invalid amount to withdraw")
elif amount > balance:
	print("Insufficient funds")
elif amount > 10000:
	print("Daily limit exceeded")
else:
	balance -= amount
	print("Transaction details")
	print(f"Debit: {amount}")
	print(f"Balance is: {balance}")
	
	
	
friends = int(input("Enter the number of friends: "))
amount = float(input("Enter amount contributed: "))
total = amount * friends
amount_to_pay = friends * 200
if friends <= 0:
	print("Invalid friends number")
else:
	if amount < 0:
		print("Invalid amount")
	elif total >= amount_to_pay:
		print(f"the money contributed is {total}")
		print(f"The amount to pay is {amount_to_pay}")
		balance = total - amount_to_pay
		print(f" the amount remain after payment is {balance}")
		balance /= friends
		print(f"Each person will get {balance}")
	elif total < amount_to_pay:
		amount_to_add = amount_to_pay - total
		print(f"The amount to add is {amount_to_add}")
	else:
		print("Thanks for your patronage")
		


first_number = float(input("First Numbers: "))
second_number = float(input("Second Number: "))
operator = input("Enter Operator: (+,-,/,*)")

if operator == '+':
	result = first_number + second_number
	print("Sum", result)
elif operator == '-':
	result = first_number - second_number
	print("Result", result)
elif operator == '*':
	print("Result", first_number * second_number)
elif operator == '/':
	if second_number == 0:
		print("Zero division error")
	else:
		print("Result", first_number / second_number)
else:
	print("Invalid Operator")



#match == switch

first_number = float(input("First: "))
second_number = float(input("Second: "))
operator = input("Operator(+,-,*,/)")

  match operator:
	case "+":
		print("Son", first number + second number)
	case "*"
		print("Result", second number first number) case "-":
		print("Result", first number-second_umber) case "/"if second number > Ge
	case
	print(first number / second number)
	print("Invalid operator")
	


first_number = float(input("First Number: "))
second_number = float(input("Secon Number: "))
operator = input("Operation (e.g Add, Sub, Mul)")
#tuple data type
operations = (operator.lower(), first_number, second_number)
match operations:
	case ("add", x,y):
		print("Result",x+y)
	case ("Sub", x,y):
		print("Result", x-y)
	case ("mul", x,y):
		print("Result", x * y)
	case _:
		print("Invalid operation")
		
"""

details = {}
name = input("Enter Your name: ")
score = int(input('Enter your Score: '))
details["name"] = score
details.update
print(details)
match details:
	case {"name": name, "score": score} if score>=70 and score<=100:
		print("student name", name)