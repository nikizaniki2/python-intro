#DONE: A Bank Account

class BankAccount:
    #Constructor takes a name for the account, initial balance and a currency.
    def __init__(self, name, balance, currency):
        #If balance is negative number, raise an ValueError error.
        if balance < 0:
            raise ValueError("ValueError negative balance")

        self.name = name
        self.balance = balance
        self.currency = currency
        self.history = ["Account was created"]
    
    #deposit(amount) - deposits money of amount to your balance.
    def deposit(self, amount):
        #If amount is negative number, raise an ValueError error.
        if amount < 0:
            raise ValueError("ValueError negative amount")
        self.balance += amount
        self.history.append("Deposited " + str(amount) + str(self.currency))
    #balance() - returns the current balance
    def get_balance(self):
        self.history.append("Balance check -> " + str(self.balance) + str(self.currency))
        return self.balance

    #withdraw(amount) - takes amount money from the account
    def withdraw(self, amount):
        if self.balance < amount:
            self.history.append("Withdraw for " + str(amount) + str(self.currency) + " failed.")
            return False
        self.balance -= amount
        self.history.append(str(amount) + str(self.currency) + " was withdrawed")
        #Returns True if it was successful. Otherwise, False
        return True

    #__str__ should print: "Bank account for {name} with balance of {amount}{currency}"
    def __str__(self):
        info = "Bank account for " + str(self.name) + " with balance of " + str(self.balance) + str(self.currency)
        print(info)
        return info
        
    
    #__int__ should return the balance of the BankAccount
    def __int__(self):
        self.history.append("__int__ check -> " + str(self.balance) + str(self.currency))
        return self.balance
    
    #transfer_to(account, amount) - transfers amount to account.
    def transfer_to(self, account, amount):
        if account.currency not in self.currency:
            #if they both have the same currencies!
            return False

        if self.withdraw(amount):
            account.deposit(amount)
            self.history.append("Transfer to " + account.name + " for " + str(amount) + str(self.currency))
            account.history.append("Transfer from " + self.name + " for " + str(amount) + str(self.currency))
            #Returns True if successful.
            return True
        return False

    #history() - returns a list of strings, that represent the history of the bank account.
    get_history = lambda self: self.history