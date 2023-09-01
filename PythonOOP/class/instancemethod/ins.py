#instance method

class Account:

    def get_details(self):          #when we are using self it means it is instance method
        print("instance method")

a1=Account()
a1.get_details()