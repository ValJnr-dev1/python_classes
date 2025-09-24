'''
number = 15
if number > 20:
	print(f"{number} is greater")
if number > 10:
	print(f"{number} is greater than 10")
if number > 5:
	print(f"{number} is less 10")
if number > 14:
	print("14 is less than number")

number = 15
if number > 20:
	print(f"{number} is greater")
elif number > 10:
	print(f"{number} is greater than 10")
elif number > 5:
	print(f"{number} is less than number")
elif number > 14:
	print(f"{number} is less than number")
else:
	print("invalid number")
	


flag = False
for number in range(1, 5):
	if number == 2:
		flag = True
		break
if flag:
	print(number, "valued")
else:
	print("number not valid")p

flag = False
names = ["Tom", "Jerry", "Mimi", "Val"]
user_name = input("Username\n>>>")
for name in names:
	if user_name in names:
		flag = True
		break
if flag:
	print("Vip")
else:
	print("Regular").
'''
numbers = [12, 75, 150, 180, 145, 525, 50]
"""
count = len(numbers) - 1
for number in range(len(numbers)):
	print(numbers[count])
	count = count - 1

largest = numbers[0]

for number in numbers:
	if number > largest:
		largest = number
print(largest)


students = []

for student in range(1, 4):
	name = input("Enter Your Name")
	gender = input("Enter Your Gender: e,g(M for Male, F for Female): ")
	score = input("Enter Your score")
	students.append({"Name": name, "gender": gender, "score": score})
print(students)




orders = [
   {"order_id": 101, "customer": "John", "items": 3, "total_price": 75},
   {"order_id": 102, "customer": "Mary", "items": 10, "total_price": 180},
   {"order_id": 103, "customer": "Alex", "items": 2, "total_price": 50},
  {"order_id": 104, "customer": "Grace", "items": 15, "total_price": 600},
  {"order_id": 105, "customer": "Paul", "items": 5, "total_price": 145}
  ]
for customers in orders:
	if customers["total_price"] > 500:
		break
	elif customers["total_price"] >= 140 and customers["total_price"] <= 200:
		continue
	else:
		if customers["items"] > 5:
			print(customers["customer"])
"""

post = [
    {"post": "House"},
    {"post": "Welcome"},
    {"post": "Bye"}
]

for i in post:
	if "Welcome" in i["post"]:
		print(i["post"])
