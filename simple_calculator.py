#a simple calculator
print ("""******************
1.Addition
2.subtraction
3.Multiplication
4.Division
*********************""")
print("Enter two numbers to add")
#prompt user for a number
first_number = input("First Number: ")
#prompt the user for number
second_number = input("Second Number: ")
sum = float(first_number) + float(second_number)
print(f"{first_number} + {second_number} = {sum:.2f}")



print("Enter two numbers to subtract")
#prompt user for a number
first_number = input("First Number: ")
#prompt the user for number
second_number = input("Second Number: ")
subtract = float(first_number) - float(second_number)
print(f"{first_number} * {second_number} = {subtract:.2f}")


print("Enter two numbers to multiply")
#prompt user for a number
first_number = input("First Number: ")
#prompt the user for number
second_number = input("Second Number: ")
multiply = float(first_number) * float(second_number)
print(f"{first_number} * {second_number} = {multiply:.2f}")


print("Enter two numbers to divide")
#prompt user for a number
first_number = input("First Number: ")
#prompt the user for number
second_number = input("Second Number: ")
divide = float(first_number) / float(second_number)
print(f"{first_number} / {second_number} = {divide:.2f}")


print("Enter two numbers to expontial")
#prompt user for a number
first_number = input("First Number: ")
#prompt the user for number
second_number = input("Second Number: ")
exp = float(first_number) ** float(second_number)
print(f"{first_number} ** {second_number} = {exp:.2f}")


print("Enter two numbers to floor")
#prompt user for a number
first_number = input("First Number: ")
#prompt the user for number
second_number = input("Second Number: ")
floor = float(first_number) // float(second_number)
print(f"{first_number} // {second_number} = {floor:.2f}")

