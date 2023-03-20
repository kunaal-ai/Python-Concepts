# List is a collection which is ordered and changeable. Allows duplicate members.
# List can have any data types
# Lists are mutable 

numbers = [0,'one',2,'three',4.0]
print(numbers)
print(numbers[1])

# Negative index => last value
print(numbers[-1])  

# ---------------
# SLICING
# ---------------
print(numbers[1:3]) # Exclude last index
print(numbers[:3]) # Exclude last index
print(numbers[3:]) 
print(numbers[:]) # All


# ---------------
# Add in list - Append
# ---------------
numbers.append('*append function')
print(numbers)

# ---------------
# Insert in list - insert
# ---------------
numbers.insert(6,'*insert function')

# ---------------
# Merge two lists - extend / +  can be used
# ---------------
numbers.remove('*append function')
numbers.remove('*insert function')

states = ['solid', 'liquid', 'gas']
numbers.extend(states)
print('\nExtend join 2 lists:',numbers)

# Concatinate does not change the original list elements.
print('Concatinate + 2 lists: ', numbers + states)
print('Original list changed:',numbers)

# ---------------
# Delete - del
# ---------------
del numbers[5:]
print('\n',numbers)

# ---------------
# Remove
# ---------------
numbers.remove(4.0)
print(numbers)

# ---------------
# Pop - delete from original list and return value
# ---------------
pop_element = numbers.pop(3)
print('Pop :',pop_element)
print(numbers)

# ---------------
# clear - removes all items from list
# ---------------
numbers.clear()
print(numbers)

# ---------------
# count - find variations 
# ---------------
number_of_occurrence = states.count('gas')
print(number_of_occurrence)

# ---------------
# sort - acs, desc - changes the order of original list
# ---------------
stocks_price = [112,43,23,565,3]
stocks_price.sort()
print(stocks_price)
stocks_price.sort(reverse=True)
print('Reverse order desc',stocks_price)

# ---------------
# Copy
# ---------------
copy_stock_price = stocks_price.copy()
print(copy_stock_price)

# ---------------
# Iterating
# ---------------
for i in stocks_price:
    print(i)

print(43 in stocks_price)  # check if element present in list
print(len(stocks_price))  

# ---------------
# comprehension 
# if we are creating a list from other list elements , short hand for can be used
# ---------------

# NO comprehension - create a list if stock price is < 100 
stocks_no_comprehension = []
for i in stocks_price:
    if i < 100:
        stocks_no_comprehension.append(i)
print('NO comprehension',stocks_no_comprehension)        

# with comprehension, short and sweet
stocks_list_with_comprehension = [i for i in stocks_price if i < 100]
print('WITH comprehension',stocks_list_with_comprehension)