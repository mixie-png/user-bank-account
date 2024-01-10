class User:
    # Attributes
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
        # self.account = BankAccount(int_rate=0.02, balance=0) #Links the User and BankAccount classes
        self.accounts = []

    # Methods
    def create_account(self, int_rate, balance):
        new_account = BankAccount(int_rate=int_rate, balance=balance) #Links the User and BankAccount classes
        self.accounts.append(new_account)
        return self

    def make_deposit(self, account_index, amount):
        # self.account.deposit(100)		# we can call the BankAccount instance's methods
        self.accounts[account_index].deposit(amount)
        print(self.accounts[account_index].balance)		# or access its attributes
        return self

    def make_withdrawal(self, account_index, amount):
        self.accounts[account_index].withdraw(amount)		# we can call the BankAccount instance's methods
        print(self.accounts[account_index].balance)		# or access its attributes
        return self

    def display_user_balance(self, account_index):
        self.accounts[account_index].display_account_info()
        return self

    def transfer_money(self, amount, other_user, account_index):
        self.accounts[account_index].withdraw(amount)
        other_user.accounts[account_index].deposit(amount)
        return self


    def display_info(self):
        print("First Name:" , self.first_name , "Last Name:" , self.last_name , "Email:" , self.email , "Age:" , self.age, "Enrolled:", self.is_rewards_member, "Current Gold Points:", self.gold_card_points)
        for account in self.accounts:
            print("Account Balance:", account.balance)
        return self

    def enroll(self):
        if self.is_rewards_member != False:
            print("Already a member")
        else:
            self.is_rewards_member = True
            self.gold_card_points = 200
        return self

    def spend_points(self, amount):
        if amount < self.gold_card_points:
            self.gold_card_points -= amount
        else:
            print("Insufficient points")
        return self

##########################################################################
class BankAccount:
    # class attribute - a list of all the accounts!
    all_accounts = []
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance):
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)

    @classmethod
    def all_balances(cls):
        sum = 0
        # we use cls to refer to the class
        for account in cls.all_accounts:
            sum += account.balance
            print(sum)
        return sum

    def deposit(self, amount):
        # your code here
        self.balance += amount
        return self
    def withdraw(self, amount):
        # your code here
        if amount < self.balance:
            self.balance -= amount
        else:
            self.balance -= amount + 5
            print("Insufficient funds: Charging a $5 fee")
        return self
    def display_account_info(self):
        # your code here
        print(f"Balance: ${self.balance}")
        return self
    def yield_interest(self):
        # your code here
        if self.balance > 0:
            self.balance = (self.balance * self.int_rate) + self.balance
        return self


# User accounts
user1 = User("Beyonce", "Knowles", "beyonce@gmail.com", 42)
user2 = User("Rihanna", "Fenty", "rihanna@gmail.com", 35)
user3 = User("Lori", "Harvey", "lori_harvey@gmail.com", 26)

user1.create_account(int_rate=0.02, balance=100).create_account(int_rate=0.02, balance=200)

user1.display_info()
user2.display_info()

user2.create_account(int_rate=0.02, balance=100).create_account(int_rate=0.02, balance=200)

user1.transfer_money(50, user2, 0)

user1.display_info()
user2.display_info()