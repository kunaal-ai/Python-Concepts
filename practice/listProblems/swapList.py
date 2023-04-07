'''
program to swap two elements in a list
e.g: 
Input : List = [23, 65, 19, 90], pos1 = 1, pos2 = 3
Output : [19, 65, 23, 90]
'''
def swap_values(user_list, pos1, pos2):
    pos1 = pos1-1
    pos2 = pos2-1
    user_list[pos1], user_list[pos2] = user_list[pos2], user_list[pos1]
    return user_list


print(swap_values([23, 65, 19, 90],1,3))
