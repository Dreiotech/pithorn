class Mpesa:
    def __init__(self,account_balance,phone_number):
        self.account_balance=account_balance
        self.phone_number=phone_number
    def send_money(self,amount,receipient):
       if self.account_balance>=amount:
          self.account_balance-=amount
          print(f"{amount} KES sent to {receipient} successfully")
       else:
           print("insufficient Amount to send money ")
class PersonalMpesa(Mpesa):
    def __init__(self,account_balance,phone_number,idno):
        super().__init__(account_balance,phone_number)
        self.idno=idno
    def buyairtime(self,amount):
        self.account_balance-=amount
        print(f"{amount} KES airtime bought successfully")
class BusinessMpesa(Mpesa):
    def __init__(self,account_balance,phone_number,business_name):
        super().__init__(account_balance,phone_number)
        self.business_name=business_name
    def receive_payment(self,amount):
        self.account_balance+=amount
        print(f"{amount} KES received from a customer")
personal=PersonalMpesa(account_balance=2000,phone_number=786456321,idno=4567789)
personal.send_money(amount=1500,receipient=8905643)
personal.buyairtime(amount=450)

business=BusinessMpesa(account_balance=4000,phone_number=789909099,business_name="Mekl")
business.send_money(amount=3000,receipient=567890)
business.receive_payment(amount=2300)