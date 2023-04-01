class GeneratePassword:
    def __init__(self) -> None:
        self.char = 25

    def get_length(self):
        return self.char

quick_password = GeneratePassword()
print(quick_password.get_length())       