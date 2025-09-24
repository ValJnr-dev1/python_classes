'''
favorite_movies = ["Merlin","Perky Blinders","Games Of Thrones","John Wick","all of us are dead","fear street"]
numbers = [1,2,3,4,5,6,7,8,9,10]
details = ["Dakshak",10,False,"Red"]
print(f"My favorite movies are {favorite_movies}")
print(numbers)
print(f"My details are {details}")


code = ["x", "H", "e", "z", "l", "l", "!", "p", "o", "-", "n", " ", "W", "@", "r", "d", "o", "#"]
print(f"{code[1]}{code[2]}{code[4]}{code[5]}{code[8]}")
print(f"{code[-6]}{code[-2]}{code[-4]}{code[4]}{code[-3]}")
print(code[::-1])
grid = [
	["The", "sky", "is"],
	["full", "of", "stars"],
	["shining", "bright", "tonight"]
]

first_list = grid[0]
second_list = grid[1]
third_list = grid[2]

print(f"{first_list[0]} {first_list[1]}")
print(f"{first_list[0]} {second_list[-1]} are {third_list[0]}")
print(second_list[::-1])



playlist = ["Song A", "Song B", "Song C"]
print(playlist)
playlist[1] = "Song D"
print(playlist)
playlist.append("Song E")
print(playlist)
playlist.insert(0, "Intro")
print(playlist)

desks = []
first_name = input("Enter the first student Name: ")
second_name = input("Enter the second student Name: ")
third_name = input("Enter the third student Name: ")
desks.append(first_name)
desks.append(second_name)
desks.append(third_name)
print(desks)
second_name = input("Enter the new name: ")
desks[1] = second_name
print(desks)
fourth_name = input("Enter the forth name: ")
desks.insert(1, fourth_name)
print(desks)


#23rd July
countries = ["spain", "Malawi", "Iran", "Usa"]
details = countries[0:3]
country1, country2 = countries[0:2]
print(country1)
print(country2)
print(details)
'''

accounts = [
	["1001","Joy", "Savings", 1500],
	["1002", "David", "Current", 2000],
	["1003", "Ruth", "Savings", 1800]
]
print(accounts)
first_account = accounts[0]
second_account = accounts[1]
third_account = accounts[2]
accounts.remove(accounts[1])
print(accounts)

name, account_type = third_account[1:3]
print(name, account_type)

name2 = first_account[1:2]
account_type1 = first_account[2:3]
print(name2, account_type1)
