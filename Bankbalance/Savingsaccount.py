from Bankaccount import Bankaccount

class Savingaccount(Bankaccount):
    pass 
    def __init__(self, accountnumber, balance, interestrate):
        super().__init__(
            accountnumber,
            balance
        )

        self.intestest_rate = interestrate

    def calculate_interest(self):
        interest = self.get_balance() * (self.intestest_rate/100)
        self.deposit(interest)

    def display_account_type(self):
        print("It is a saving account")

arunsavingaccount = Savingaccount("111", 900)


