class GeneratePassword:
    def __init__(self, charact_limit) -> None:
        self.char = charact_limit

    def get_length(self):
        return self.char


strong_password = GeneratePassword(15)
print(strong_password.get_length())
