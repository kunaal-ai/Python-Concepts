import csv

name=input("Enter name: ")
home=input("Enter home address: ")

# a - append mode, open and append input 
with open("file_io/user_values.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name","home"])
    writer.writerow({"name":name, "home":home})
