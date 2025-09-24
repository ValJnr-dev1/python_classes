student = {
"name": "Tom",
"department": "Computer Science",
"grades": [{"csc 111": 90, "Maths 111": 50, "Physics":70}],
"address": {"city": "Jos", " town": "Rayfield", " house-no": "Pl/Ray/0415"},
"fav_color": [" pink", "Red", "Black", "White"]
}

print(student)
#accesing dictionary items
print(student["name"])
print(student["department"])
print(f"csc 111 score: ", student["grades"][0]["csc 111"])
print("Fav color: ",  student["fav_color"][2])
#dictionary meth
print(student.get("name"))
#print(student.key())
print(student.items())

print("=======updating student data======")
student["name"] = "Jerry"
new_name = {
"surname": "Joy",
"name": "Mercy"
}
#kwargs **, Positional argument *
student.update(new_name)
print(student)


#To delete an Item
print("============")
student.popitem()
print(student)
student["fav_color"].remove("Red")
print(student)


