#Creating to variables
my_age = 23
pi = 3.14159
magic_number = ((my_age * 3 + pi) % 7)
print("The type of magic number is:",type(magic_number))
print(magic_number)

#Slicing
secret_word = "PythonIsAmazing"
print("The first six characters of the string is:",secret_word[-16:-9])
print("The last seven characters of the string is:",secret_word[-7:])
print("The middle word is:",secret_word[-9:-7])
print("The reverse string is:",secret_word[::-1])
print("Every second character of the string is:",secret_word[::2])

#casing
upper_case = secret_word[-16:-9].upper()
lower_case = secret_word[6:].lower()
print(upper_case)
print(lower_case)
print(upper_case + lower_case)

