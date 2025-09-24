'''
for num in range(1, 100):
	if num % 2 == 0:
		if num >= 60 and num <= 70:
			continue
print(num)



password = 1525
if password == 1525:
	print("correct password")
if password != 1525:
	print("Incorrect password")
	
'''
"""
	18-25= regular
	26-35=vip
	36-40=vvip
	
age = int(input("Age: "))
if age>=18 and age<=25:
		print("Regular")
elif age>=26 and age<=35:
		print("VIP")
elif age>=36 and age<=45:
		print("VVIP")
else:
	print("You are not welcome")


amount = int(input("Enter your amount: "))
discount = 0

if amount> 50000:
	discount = (amount * 20)/100
	print(f"Your disclount is {discount}")
	final_payment = (discount - amount)
	print(f" final amount to pay {final_payment} ")
elif amount>30000 and amount<= 50000:
	discount = (amount * 10)/100
	print(f"Your discount is {discount}")
	final_payment = (discount - amount)
	print(f" final amount to pay {final_payment} ")
elif amount>= 10000 and amount<=30000:
	discount = (amount * 2)/100
	print(f"Your discount is {discount}")
	final_payment = (discount - amount)
	print(f"final amount to pay {final_payment} ")
else:
	print("No Discount")
	print(f"You will pay {amount}")


print('''
1. Onboard custumer 
2. Withdraw 3Add Cahs
4. Transfer
5. Change Pin
''')
customer = []
automatic_id
user_input = int(input("select an Operation: "))
if user_input >=1 and user_input <=5:
	if user_input == 1:
		user_name = input("Name: ")
		user_amount = float(input("Enter Amount: "))
		user_pin = input("Pin")
		if len(user_pin) == 4:
			new_customer = {"name":  user_name,"amount": user_amount, "pin": int(user_pin), "id": automatic_id}
			automatic_id += 1
			customer.append(new_customer)
		else:
			print("Invalid pin lenght")
	if user_input == 2:
			user_id = int(input("id: "))
			amount 
			
			
			
else:
	print("Invalid selected operation")
print(customer)


score = int(input("Enter Your jamb score: "))

if score>=250 and score <=400:
	print("Eligible for Medicine")
elif score>200 and score<=249:
	print("Eligible for Engineering or science")
elif score>=180 and score <=199:
	print("Eligible for education or social scince")
elif score<180 and score>=0:
	print("Not eligible for admission")
else:
	print("invalid score")


money = int(10000)
money_withdraw = float(input("Enter how much you want to withdraw: "))
if money_withdraw >= 1 and money_withdraw % 1000==0 and money_withdraw<=10000:
	
	print("withdrawal successful")
	money -= money_withdraw
	print(f"Your Balance is {money}")
else:
	print("Invalid Amount or insufficient funds")
"""

money = int(10000)
money_withdraw = float(input("Enter how much you want to withdraw: "))
"""
if money_withdraw >= 1 and money_withdraw % 1000==0 and money_withdraw<=10000:
	
	print("withdrawal successful")
	money -= money_withdraw
	print(f"Your Balance is {money}")
else:
	print("Invalid Amount or insufficient funds")
"""
if money_withdraw == 0:
	print("Amount to small")
	if money_withdraw < 0 and money_withdraw> money:
		print("Invalid amount")
		if money_withdraw %1000==0:
			print("Withdrawal successful")
			money -= money_withdraw
			print(f"Your balance is {money}")
else:
	print(f"Input amount between 1000 to {money}")