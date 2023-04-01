# optional has to be at last only
def optionalArguments(prog_language, rating, in_use=''): 
    result = ''
    if in_use:
        result = f" Language {prog_language} is holding {rating} star rating and using in company {in_use}"
    else:
        result = f" Language {prog_language} is holding {rating}"
    return result    

print(optionalArguments('Python',5))       
print(optionalArguments('Python',5,True))       