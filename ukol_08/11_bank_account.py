'''vytvořte soubor
v něm třídu BankAccount, který reprezentuje bankovní účet
třída bude mít attributy
- číslo účtu (str nebo int)
- majitel (stačí jako str)
- stav (konto)

metody
- vložit peníze
- odebrat peníze
- tisknout stav konta

názvy atributů a method vhodně vymyslete
'''

# create class BankAccount
class BankAccount:
    def __init__(self, account_number, owner, balance=0):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance

# create methods
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit of {amount} was successful."
              f"\n Actual balance is {self.balance}."
              f"\n Name of owner is {self.owner} (account ID is {self.account_number})."
              f"\n Thank you for using our services.")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrawal of {amount} was successful."
                  f"\n Actual balance is {self.balance}."
                  f"\n Name of owner is {self.owner}."
                  f"\n Thank you for using our services.")
        else:
            print(f"Sorry, Insufficient funds. Go work!"
                  f"\n Actual balance is {self.balance}."
                  f"\n Name of owner is {self.owner}."
                  f"\n Thank you for using our services.")



    def print_balance(self):
        print(f"Account number: {self.account_number} owned by {self.owner} has balance of {self.balance}."
              f"\n Thank you for using our services.")


# create instances
client_1 = BankAccount(123456, "Petr", 1000)
client_2 = BankAccount(654321, "Jan", 2000)
client_3 = BankAccount(987654, "Nina")

# test methods
client_1.deposit(500)
client_2.withdraw(5000)
client_3.print_balance()