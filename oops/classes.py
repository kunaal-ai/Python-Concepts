class Calculations:
    def __init__(self, no_a, no_b):
        self.number_a = no_a
        self.number_b = no_b

    def addition(self):
        return self.number_a + self.number_b

    def multiplication(self):
        return self.number_a * self.number_b

    @staticmethod  # these dont need and can not access class data
    def debug_statement(name):
        print("This is debug sample statement passed by", name)


calculate = Calculations(2, 10)
print(calculate.addition())
print(calculate.multiplication())
calculate.debug_statement("QA Engineer")
