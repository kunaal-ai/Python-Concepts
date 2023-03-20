'''
upper
lower
partition
replace
rstrip - removes white trailing spces
split
startswith
isnumeric - check is all characters are numeric
find - returns first accurance index value, -1 if found none
index - returns first accurance index value, value error exception if found none
'''

description = 'I am working as an automation is engineer from last 5 years. This is string in python.'
print(description.upper())
print(description.lower())
print(description.partition('.'))
print(description.replace('automation engineer', 'QA engineer'))
print(description.rstrip())
print(description.split(' '))
print(description.startswith('I'))
print(description.isnumeric())
print(description.find('is'))
print(description.index('is'))

# ----------------
# f-string
# ----------------
language = 'python'
purpose = 'automation'
print(f'I am using {language} for web {purpose}')