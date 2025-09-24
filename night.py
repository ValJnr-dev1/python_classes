'''
favorite = ["Merlin", " GOT", "Sonic", "SUperman"]
numbers = [1,2,3,4,5,6]
details = ["Dakshak", 15, False, 1.70]
print(f"My Favorite Movies are {favorite}")
print(numbers)
print(details)

code = ["x", "H", "e", "z", "l", "l", "!", "p", "o", "-", "n", " ", "W", "@", "r", "d", "o", "#"]
Hello = code[1] + code[2] + code[4] + code[5] + code[8]
print(Hello)
print(f"{code[1]}{code[2]}{code[4]}{code[5]}{code[8]}")
print(f"{Hello} {code[-6]}{code[-2]}{code[-4]}{code[4]}{code[-3]}")

grid = [
	["The", "sky", "is"],
	["full", "of", "stars"],
	["shining", "bright", "tonight"]
]
print(f"{grid[0][0]} {grid[0][1]}")
print(f"{grid[0][0]} {grid[1][2]} are {grid[2][0]}")
second_line = grid[1]
print(second_line[::-1])

playlist = ["Song A", "Song B", "Song C"]
print(playlist)
playlist[1] = "Song D"
print(playlist)
playlist.append("Song E")
print(playlist)
playlist.insert(1, "intro")
print(playlist)
playlist.remove(playlist[1])
print(playlist)


'''



Desks = []
name_one = input("Enter First Name: ")
name_two = input("Enter second name: ")
name_three = input("Enter Third Name: ")
Desks.append(name_one)
Desks.append(name_two)
Desks.append(name_three)
print(Desks)
name_two = input("Enter Name: ")
Desks[1] = name_two
print(Desks)
name_four = input("Enter New Name: ")
Desks.insert(1, name_four)
print(Desks)
