
class Account:
    def __init__(self,acount_number:str,balance:int):
        self.account_number=account_number
        self.balance=balance


class SavingAccount(Account):
    def __init__(self,interest_rate:float,account_number:str,balance:int):
        self.interest_rate=interest_rate
        super().__init__(account_number,balance)

    def add_interest(self):
        principle_with_interest = self.balance+self.balance*self.interest_rate/100
        return principle_with_interest
    
    def __repr__(self):
        return f"Account number :{self.account_number}\nPrevious Balance:{self.balance}"
    



if __name__ == "__main__":
    account_number="123ABX"
    balance=2000
    interest_rate=8
    saving_obj=SavingAccount(interest_rate,account_number,balance)
    print("-"*39)
    print("object of Saving account",saving_obj)
    print("-"*39)
    print("whole info of saving class",saving_obj.__dict__)
    print("-"*39)
    print("class whole box info of saving class",SavingAccount.__dict__)
    new_balance=saving_obj.add_interest()

    print("-"*39)
    print("representation",saving_obj.__repr__)
    print("="*39)
    print("New Balance(with interest=8%)",new_balance)