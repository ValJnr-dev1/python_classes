# class BankAccount:
#     def __init__(self, owner, balance=0):
#         self.owner = owner
#         self.balance = balance

#     def deposit(self, amount):
#         if amount > 0:
#             self.balance += amount
#             print(f"Deposited ${amount}. New balance: ${self.balance}")
#         else:
#             print("Deposit amount must be positive.")

#     def withdraw(self, amount):
#         if amount > self.balance:
#             print("Insufficient funds.")
#         elif amount <= 0:
#             print("Withdrawal amount must be positive.")
#         else:
#             self.balance -= amount
#             print(f"Withdrew ${amount}. New balance: ${self.balance}")

#     def get_balance(self):
#         print(f"Current balance: ${self.balance}")
#         return self.balance

# def main():
#     print("Welcome to Simple Bank App")
#     name = input("Enter your name: ")
#     account = BankAccount(name)

#     while True:
#         print("\nOptions: deposit, withdraw, balance, exit")
#         choice = input("Choose an option: ").lower()

#         if choice == "deposit":
#             amount = float(input("Enter amount to deposit: "))
#             account.deposit(amount)
#         elif choice == "withdraw":
#             amount = float(input("Enter amount to withdraw: "))
#             account.withdraw(amount)
#         elif choice == "balance":
#             account.get_balance()
#         elif choice == "exit":
#             print("Thank you for using Simple Bank App.")
#             break
#         else:
#             print("Invalid option. Try again.")

# if __name__ == "__main__":
#     main()

num1 = 5
num2 = num1
num1 = 10
print(id(num2))