class Bank:
    def __init__(self,id,name,sal):
        self.acc_id=id
        self.acc_name=name
        self.acc_sal=sal



b=Bank(1,'srinivas',60000)
print(b.__dict__)