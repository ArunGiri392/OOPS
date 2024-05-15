# Create a class "BankAccount" with attributes account number and balance. Implement methods to deposit and withdraw funds, and a display method to show the account details.
class Bankaccount:
    def __init__(self, accountnumber : int, balance : float):
        self.__accountnumber = accountnumber
        self.__balance = balance
    
    def deposit(self, depositamount):
        self.__balance = self.__balance + depositamount
    
    def withdraw(self, withdraw):
        if self.__balance >= withdraw:
             self.__balance = self.__balance - withdraw
        else:
            print("Insufficient funds")
    
    def accountdetails(self):
        print("Your account number is" + str(self.__accountnumber))
        print("Your current balance is " + str(self.__balance))

    def get_balance(self, pincode):
        if pincode == 5857:
            return self.__balance
        else:
            print("Your pin code is not correct, please provide a correct pincode.")
    
    def get_accountnumber(self,pincode):
        if pincode == 5857:
            return self.__accountnumber
        else:
            print("Your pin code is not correct, please provide a correct pincode.")
    
    def display_account_type(self):
        print("It is a checking account")
    
arun = Bankaccount(1234, 400)
print(arun.get_balance())
arun.deposit(1000)
arun.withdraw(100)
arun.accountdetails()