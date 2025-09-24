'''
percent = 100
phone_percent = 0

while phone_percent <= 100:
	print(f"Phone percent: {phone_percent}%")
	charge = int(input("Percent to add"))
	phone_percent += charge
	print(f"Charging: {phone_percent}")


names = ["Tom", "Jerry", "Mimi", "Val", "Kelvin"]
count = 0
list_len = len(names)
while count < list_len:
	print(names[count])
	count += 1



count = 1
while count <= 100:
	if count % 2 != 0:
		print(count)
	count += 1

'''

students = {
	"John": 60,
	"Mimi": 50,
	"Sarah": 30
}
students_keys = list(students.keys())
students_values = list(students.values())
count = 0
while count <= len(students_values) - 1:
		name = f"{students_keys[count]} = {students_values[count]}"
		print(name)
		count += 1

