# class Student:
#     def __init__(self,name,score):
#         self.name = name
#         self.score = score

#     def pass_or_fail(self):
#         if self.score >= 40:
#             return True
#         else:
#             return False
        

# section_a = Student('Test',20)
# print(section_a.name)
# print(section_a.score)
# print(section_a.pass_or_fail())


class Complex:
    def __init__(self, real , img):
        self.real = real
        self.img = img
        print(self.real)

    def add(self,number):    
        real = self.real + number.real
        img = self.img + number.img
        

a = Complex(3,4)
b = Complex(5,6)