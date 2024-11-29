class Banking:
    def __init__(self, user_name, initial_balance):
        self.user_name = user_name
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        return amount

    def get_balance(self):
        return self.balance

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return amount
        else:
            return "Insufficient Balance"

# Creating an instance of the Banking class
Hasib_Chowdhury = Banking("Hasib Chowdhury", 10000)
print(f"Account Name: {Hasib_Chowdhury.user_name}")
print(f"Initial Balance is: {Hasib_Chowdhury.balance}")
print(f"Deposit Balance: {Hasib_Chowdhury.deposit(1000)}")
print(f"Get Balance is: {Hasib_Chowdhury.get_balance()}")
print(f"withdraw Balance is: {Hasib_Chowdhury.withdraw(5000)}")
print(f"Get Balance After Withdraw : {Hasib_Chowdhury.get_balance()}")