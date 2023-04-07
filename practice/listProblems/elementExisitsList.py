'''
program to reverse a list

e.g:
Input : ['Python', 'Pytest', 'Postman','Jmeter']
Output : ['Jmeter', 'Postman', 'Pytest', 'Python']
'''
original_list = ['Python', 'Pytest', 'Postman','Jmeter']
reversed_list = list()

for item in original_list:
    reversed_list = [item] + reversed_list

print(reversed_list)
