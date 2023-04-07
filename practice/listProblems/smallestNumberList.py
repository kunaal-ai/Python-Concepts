'''
program to find smallest number in a list
'''

def smallestNumber(user_list):
    small_number = user_list[0]
    for i in user_list:
        if i < small_number:
            small_number = i
    
    return small_number


print(smallestNumber([2,1,4,3,7,0,9,5]))
