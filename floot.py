'''
height = 45/4
print(f"My height is {height:.1f}")

account_balance = 5000 / 3
print(f"Balance: {account_balance:.3f}")
height_int = float(input("Height\n >>>"))
print(f"Your Height is {height_int:.2f}")

user_account = 1000000
print(f"Balance is: ₦{user_account:,.2f}kb")

bio = "My name is Tom"
print(not "name" in bio)

print("id|\t Name|\t Gender)

print("1|\t Tom|\ Male")
print("backslash\a")


bio = "Tom is a programmer"
print(bio.startswith("Tom"))


fruits = "Apple, Mango, Orange, Banana, Kiwi"
print(fruits)
list_of_fruits = fruits.split(",")
print(list_of_fruits[3])
celebrities = "Davido- Wizkid-Rema-Portable-Buju-Burna"
list_of_celebrities = celebrities.split("-")
print(list_of_celebrities[2])

record = "James Abuja 150000.5 NGO921"

list_record = record.split(" ")
salary = float(list_record[-2])
name = list_record[0]
print(f"Name:\t\t\t{name:}")
print("Name:\t\t\t" + list_record[0])
print("Initial:\t\t" + record[0].capitalize())
print("ID:\t\t\t" + list_record[-1])
print("Valid ID:\t\t" + "Yes")
print(f"Monthly Salary:\t\t{salary:,.2f}" )

print()
print()


message = "GhostNet#X44CR#98.654#TRC8821"
print("ALERT REPORT")
print("_________________________________________")
list_message = message.split("#")
severity_level = float(list_message[-2])
print("Code Name:\t\t\t" + list_message[0])
print("Message Code:\t\t\t" + list_message[1])
print("Last Letter:\t\t\t" + message[13])
print("Trace ID:\t\t\t" + list_message[-1])
print("Traceable:\t\t\t" + "Yes")
print(f"Severity Level:\t\t\t{severity_level:.2f}" )
'''
