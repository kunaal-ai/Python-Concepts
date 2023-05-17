# Instance Method: Most common, able to access data and proprties unique to each instance.
# suppose if create 5 objects of method, python will create 5 copies. Where static method can save
# memory as it will create only 1 copy per class.
class customer_details:
    def __init__(self) -> None:
        pass

    def customer_name(self):
        print("TEST")

    # Instance method.
    def customer_id(self):
        self.customer_name()
        return 50


get_id = customer_details()
print(get_id.customer_id())
