class Employee:
    def __init__(self, first_name, last_name) -> None:
        self.first_name = first_name
        self.last_name = last_name
    @property
    def email(self):    
        return self.first_name+"."+self.last_name+"@email.com"
    
    @email.setter
    def email(self, email):
        self.email = email




obj_1 = Employee("james","carter")
print(obj_1.email)




