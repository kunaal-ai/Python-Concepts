class ReturnString:
    def __init__(self, f_name, l_name) -> None:
        self.f_name = f_name
        self.l_name = l_name

    def __str__(self) -> str:
        return f"{self.f_name} registered and last name is {self.l_name}"

print(ReturnString("John", "wick")) # otherwise this must have printed <__main__.ReturnString object at 0x102b4b990>