class TechStack:
    def __init__(self, dept) -> None:
        """Constructor"""
        self.department = dept
        self.block = "A"  # setting default value

    def department_name(self):
        return self.department

    def dep_block(self):
        return self.block


ts = TechStack("Engineering")
print(ts.department_name())
print(ts.dep_block())
