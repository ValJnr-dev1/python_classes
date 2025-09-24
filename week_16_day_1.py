def add_numbers(a, b):
    add(a, b)
    print(f"The sum of {a} and {b} is {result}")
    return result

def names(*args):
    for name in args:
        print(f"Hello, {name}!")
    return args

def calculate_age(current_year, birth_year):
    age = current_year - birth_year
    print(f"You are {age} years old.")
    return age

def num1(a):
    return a

def num2(b):
    return b

def add():
    total = num1(int(input("Enter num1"))) + num2(int(input("enter second number1")))
    print(total)
    
def calc():
    numb = []
    new_list = []
    numbers = input("Enter the numbers you want to use: ")
    for items in numbers:
        numb.append(items)
    for numb[::2] in numb:
        new_list.append()
    print(numb)
    
# calc() 

#write a *args function that takes unkown number of input with any operators and execute the operation
def calculate(*args, operator):
    if operator == "+":
        total = sum(args)
    elif operator == "-":
        total = args[0]
        for num in args[1:]:
            total -= num
    elif operator == "*":
        total = 1
        for num in args:
            total *= num
    elif operator == "/":
        total = args[0]
        for num in args[1:]:
            total /= num
    print(f"The total is {total}")
    return total

def tri_recursion(k):
    if (k > 0):
        result = k + tri_recursion(k- 1)
        print(result)
    else:
        result = 0
    return result

print("Rescuion Example Results:")
tri_recursion(6)