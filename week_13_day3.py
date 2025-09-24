
def calculate_age(year_of_birth):
    current_year = 2025
    if year_of_birth > current_year:
        return "invalid year of birth"
    return current_year - year_of_birth

def bio(name, year, gender):
    user_age = calculate_age(year)
    return {
        "name": name,
        "age" : user_age,
        "gender" : gender
    }
    
print(bio("dak", 2000, "male"))

def calculate_fact(number):
    if number == 1 or number == 0:
        return 1
    else:
        return number * calculate_fact(number - 1)
    
print(calculate_fact(5))

def calculate_fib(number):
    if number == 1:
        return 1
    elif number == 0:
        return 0
    else:
        return calculate_fib(number-1) + calculate_fib(number-2)
    
print(calculate_fib(5))