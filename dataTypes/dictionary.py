# Ordered and changeable. No duplicate members.

programming_languages = {1:'python', 2:'javascript',3:'ruby'}
print(programming_languages)

# ADD
programming_languages [0]= 'java'
print(programming_languages)

# change value
programming_languages[3] = 'typescript'
print(programming_languages)

# delete
del programming_languages[0]
print(programming_languages)

# check is key is present, does not check for values
print(2 in programming_languages)

# iteration
for i in programming_languages:
    print(programming_languages[i])


# sorted - key basis
sorted_dict = dict(sorted(programming_languages.items()))
print(sorted_dict)

# sorted - value basis , use lambda
#my_dict = {'apple': 3, 'banana': 2, 'orange': 1}
sorted_dict = dict(sorted(programming_languages.items(), key=lambda item: item[1]))
print(sorted_dict)


'''
all
any
len
sorted
clear
keys
values
'''