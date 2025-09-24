'''
#for variable-intialisation iterable:
	<body>
	</body>
	


numbers = [1, 2, 3, 4, 5]
vip = ["Tom", "Jerry", "Mimi", "Val", "John"]
for i in range(5):
	names = input("Enter your name: ")
	if names in vip:
		print("VIP")
	else:
		print("regular")
		


for i in range(1, 101):
	if i % 3 == 0 and i % 5 ==0:
			print(f"{i} FizzBuzz")
	elif i % 5 == 0:
		print(f"{i} Buzz")
	elif i % 3 == 0:
		print(f"{i} Fizz")
	else:
			print(i)
			
'''
students = {
   "S001": {"name": "John Doe", "age": 20, "score": 85},
    "S002": {"name": "Jane Smith", "age": 19, "score": 92},
    "S003": {"name": "Michael Brown", "age": 21, "score": 78},
   "S004": {"name": "Emily Davis", "age": 22, "score": 88},
   "S005": {"name": "Daniel Johnson", "age": 20, "score": 95},
    "S006": {"name": "Sarah Wilson", "age": 18, "score": 81},
   "S007": {"name": "David Lee", "age": 23, "score": 76}
}
age = int(input("Enter age:"))
for i in students:
	if age == students[i]["age"]:
		print(students[i])
	