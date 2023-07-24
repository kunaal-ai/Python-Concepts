filename = '../Python-Concepts/test_document.txt'

with open(filename) as file:
    for i, line in enumerate(file):
        print(f"{i+1}:{line}", end="")