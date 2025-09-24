'''
student_1 = {
"name": "Tom",
"university": "Uj",
"department": "Cs"
}

print("student 1", student_1)

student_2 = student_1
student_2["name"] = "Kelvin"

print(student_2)
print("student 1", student_1)
'''
foods = {
"Gote": "available", 
"dankali": "available", 
"bibal": "availble", 
"Yam": "avalable", 
"Rice": "available"
}

check_available_food = (foods.get(input("input the food you want to check")))!= None
print(check_available_food)