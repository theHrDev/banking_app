class Customer:
    def __init__(self,id,name,email,phone,accounts):
        self.id = id
        self.name = name
        self.email = email
        self.phone = phone
        self.accounts = accounts
        
class Account:
    def __init__(self,account_number,balance,owner_id,transactions):
        self.account_number = account_number
        self.balance = balance
        self.owner_id = owner_id
        self.transaction = transactions
    
class Transaction:
   def __init__(self,id,type,amount,data,from_account,to_account):
       self.id = id 
       self.type = type
       self.amount = amount
       self.data = data
       self.from_account = from_account
       self.to_account = to_account