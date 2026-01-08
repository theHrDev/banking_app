class Customer:
    def __init__(self,id,name,email,phone,accounts):
        self.id = id
        self.name = name
        self.email = email
        self.phone = phone
        self.accounts = accounts
        
class Account:
    def __init__(self):
        pass
    
class Transaction:
   def __init__(self,id,type,amount,data,from_account,to_account):
       self.id = id 
       self.type = type
       self.amount = amount
       self.data = data
       self.from_account = from_account
       self.to_account = to_account