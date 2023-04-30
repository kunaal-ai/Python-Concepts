"""
Set is a collection which is unordered, unchangeable/immutable, and unindexed. No duplicate members.
unordered, hence cannot access or change an element of a set using indexing or slicing.
"""
employee_id = {1122, 34, 1122}
print(employee_id)


# empty set declaration
emp_account_id = set()
emp_account_id = {4444,5555,6666,7777,1111}
print(emp_account_id)

# -----------
# ADD
# -----------
employee_id.add(9999)
print(employee_id)

# -----------
# Update - merge set 2 in set 1
# -----------
employee_name = {'James','Carter','Lues'}
employee_name.update(employee_id)
print('Update :',employee_name)

# -----------
# discard - remove element
# -----------
employee_name.discard('Lues')
print('Discard lues:',employee_name)

for e in employee_name:
    print(e)


# -----------
# SET operations
# -----------
# Union
# Intersection
# Difference
# Symmetric Difference
# == (equal)

# union | => all elements of sets ignore duplicate elements
a = {1,3,5,6}
b = {0,2,4,6}
print('Union | :',a|b)

# intersection => only common element
print('intersection &: ', a&b)

# difference => include elements of 1 if not present in 2
print('difference a-b: ',a-b)
print('difference b-a: ',b-a)

# symmetric difference => includes all elements of A and B without the common elements.
print(a^b)
print(b^a)

# equal ==
c = {1,2,3}
d = {1,2,3}
print(c==d)






































































































































































































































































































































































































