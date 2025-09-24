# print("this python script acts as a micro-wave")
import time
print ("**********************")
print ("Welcome to Cohort III Micro-wave") 
print ("**********************")
print ("1. Open the micro-wave")
print ("2. put the rice")
print ("3. set time")
customer = {}
name = input("Enter your name: \n>>>>")
customer["name"] = name
time_to_micro_wave = int(input("duration: \n>>>>"))
convert_to_int=float (time_to_micro_wave)
customer["duration"] = convert_to_int
price_to_pay = convert_to_int * 1000
customer["amount"] = price_to_pay
print("You are charge", price_to_pay,"")
print("Your rice will ready in {} min(s) {}".format(convert_to_int, name)) # or (f"your rice will be ready in {convert_to_int} min(s) {username}
print ("4. i will let you know when it is ready")
print(customer)
minutes_in_seconds =60
time.sleep(time_to_micro_wave * 60)
print ("5. your food is ready")
