class Account:
    def __init__(self,acc_no,name,balance):
        self.acc_no = acc_no
        self.name = name
        self.balance = balance
    def deposite_money(self,dep_amnt):
        self.balance = self.balance + dep_amnt
        return self.balance
    def withdraw_money(self,with_amnt):
        
        if self.balance - with_amnt < 1000:
            return 0
        elif self.balance < with_amnt:
            return 'insufficient amount'
        else:
            self.balance = self.balance - with_amnt
            return self.balance

acc_no=int(input())
name = input()
balance = float(input())

obj = Account(acc_no,name,balance)

t_type = input()
if t_type == 'd':
    dep_amnt = int(input())
    amount=obj.deposite_money(dep_amnt)
    print(amount)
else:
    with_amnt = int(input())
    bal = obj.withdraw_money(with_amnt)
    print(bal)