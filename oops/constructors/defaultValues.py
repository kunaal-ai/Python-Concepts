class GeneratePassword:
    def __init__(self, start_with="K", ends_with="T") -> None:
        self.start_with = start_with
        self.ends_with = ends_with

    def assemble_password(self):
        password = self.start_with + "junk_added" + self.ends_with
        return password


getPassword = GeneratePassword(start_with="Parameter Passed")
print(getPassword.assemble_password())
