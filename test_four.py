'''
#Question 1
bio = input("Enter Your bio: ")
print(len(bio))

bio_slipt =bio.split()
print(bio_slipt[0:20])
bio2 = bio_slipt[-21:-1]
print(bio2[-20:])
print(len(bio2))

#Question 2

bill = float(input("Enter Total bill: "))
num_people = int(input("Enter Number of friend: "))
bill_per_person = bill / num_people
print(f"Each person will pay ${bill_per_person}")


#Question 3
favorite_movie = input("Enter Your Favorite Movie: ")
number_times_watch = int(input("Enter The Number Of Times You Watch The Movie: "))
print(f"I've watch the {favorite_movie} {number_times_watch} times")
print(favorite_movie.upper())
print(favorite_movie[-3:])

#Question 4

total_steps_monday = float(input("Enter the number of steps you did on monday: "))
total_steps_tuesday = float(input("Enter the number of steps you did on tuesday: "))
total_steps_wednesday = float(input("Enter the number of steps you did on wednesday: "))
average_steps_per_day = (total_steps_monday + total_steps_tuesday + total_steps_wednesday) / 3
total_steps = total_steps_monday + total_steps_tuesday + total_steps_wednesday
print(f" You walked a total of {total_steps:,} steps in 3 days. That's an average of {average_steps_per_day:,} steps per day")
'''
#Question 4

password = input("Enter Your password")
print(len(password))
print(password[0],password[-1])
total_len = len(password)
total_stars = password[0] + ((total_len - 2) * ("*")) + password[-1]
print(total_stars)
