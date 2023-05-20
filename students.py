"""module Docs
"""
class Student:
    """class Docs"""

    def __init__(self, name, house):
        self.name = name
        self.house = house

    def __str__(self) -> str:
        return "String"


def main():
    """_summary_"""
    print("In main")
    student = get_student()
    print(student)


def get_student():
    """_summary_

    Returns:
        _type_: _description_
    """
    name = input("name ")
    house = input("house ")
    return Student(name, house)


if __name__ == "__main__":
    main()
