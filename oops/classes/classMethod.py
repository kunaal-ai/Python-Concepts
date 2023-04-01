## Decorators:
# Class Method: can access limited methods in class. Can modify class related details.
# can call other static methods

class customer_details:
    def __init__(self) -> None: # constructor method
        print('constructor is done')

    def customer_verification(self):
        pass

    @classmethod  
    def cash_back(cls,amount):
        print(amount * 2)
    

get_id = customer_details()
get_id.cash_back(100)   