class BankAccount:
    def __init__(self,name,balance):
        self.name=name #public
       # self._balance=balance #protected
        self.__balance=balance #private=>data mangling
    def get_balance(self): #getter
        return self.__balance
acc1=BankAccount("Rahul Kumar",100_000)
#print(f"Account name is {acc1.name} and balance is {acc1.__balance}")
print(f"Account name is {acc1.name} and balance is {acc1.get_balance()}")