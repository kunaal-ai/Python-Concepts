# can take as many arguments 

# *args - return as tuple
def arbitraryArguments(prog_language, rating, *args):
    result = f"language = {prog_language} rating is {rating} and extra details {args}"
    return result

print(arbitraryArguments('a',3,'a','r','g','s'))

# **kwargs - return as dictionay

def arbitraryArgumentsDic(prog_language, rating, **kwargs):
    kwargs['language']=prog_language
    kwargs['star_rating']=rating
    return kwargs

response = arbitraryArgumentsDic('python',3,level='master', years_of_exp=5)
print(response)