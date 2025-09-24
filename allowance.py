allowance = 2000
print(f"My allowance is ${allowance}")
books_exp = 400
print("i spent $400 on my books")
allowance -= 400
print(f"My current allowance balance is ${allowance}")
print("Just got $100 under my bed")
allowance += 100
snacks_exp = 250
allowance -= 250
print(f"i just spent $250 on snacks. My allowance is remaining ${allowance}")
siblings_exp = 25
allowance -= ((allowance *25) / 100)

print(f"my allowance is left ${allowance}")
allowance -= ((1/3) * allowance)
print(f"My current balance is ${allowance}")
allowance //= 2
print(f"my allowance is ${allowance}")
allowance %= 100
print(f"allowance remain ${allowance}")

