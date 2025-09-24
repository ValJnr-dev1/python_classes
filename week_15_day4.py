#import os
#get user quote
#get user file name
#seperate the user filename from the extention
#Write a code that checks the extention if its the required extention if the extention is correct then create the file else it should ask for the right extention

# num1, num2, num3 = 1, 2, 3

# user_input = 5
# if type(user_input) == int:
#     print(f"Your value {user_input} is of type int")
# elif type(user_input) == str:
#     print(f"Your value {user_input} is of type str")
# elif type(user_input) == float:
#     print(f"Your value {user_input} is of type float")
# elif type(user_input) == dict:
#     print(f"Your value {user_input} is of type dict")
# elif type(user_input) == tuple:
#     print(f"Your value {user_input} is of type tuple")
# elif type(user_input) == set:
#     print(f"Your value {user_input} is of type set")
# elif type(user_input) == bool:
#     print(f"Your value {user_input} is of type Bool")
# elif type(user_input) == None:
#     print(f"Your value {user_input} is of type None")
# elif type(user_input) == bytes:
#     print(f"Your value {user_input} is of type bytes")
# elif type(user_input) == range:
#     print(f"Your value {user_input} is of type range")
# else:
#     print("Unknown type")

# Value = "A"
# value_type = type(Value)
# print(f"The datatype of {Value} is {value_type}")

# import random

# random_num = random.randrange(1, 10)
# user_input = int(input("Enter your number choice"))
# if user_input == random_num:
#     print("You win")
# else:
#     print("Try again")

user_input = input("Enter your email: ")
valid_email = "@" in user_input
if valid_email:
    print(user_input)
else:
    print("Invalid email")
