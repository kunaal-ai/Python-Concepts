'''
Program to find sum and average of List in Python
Input: [4, 5, 1, 2, 9, 7, 10, 8]
Output:
sum =  46
average =  5.75
'''
def find_sum_average(user_list):
    sum = 0
    for i in user_list:
        sum += i
    average = sum/len(user_list)
    return [sum,average]    


print(find_sum_average([4, 5, 1, 2, 9, 7, 10, 8]))  