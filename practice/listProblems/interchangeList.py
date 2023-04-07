'''
program to interchange first and last elements in a list

e.g:
Input : [82, 15, 39, 26, 4]
Output : [4, 15, 39, 26, 82]

Input : [1, 2, 3]
Output : [3, 2, 1]
'''

def swap_values(elements_list):
    elements_list[0], elements_list[-1] = elements_list[-1], elements_list[0]
    return elements_list


print(swap_values([1,2,3,4]))
print(swap_values([82, 15, 39, 26, 4]))