"""Explaining use of *args and **kwargs
"""


def arbitrary_arguments(prog_language, rating, *args):
    """*args can take x no. of arguments
    return as tuple
    """
    result = f"language = {prog_language} rating is {rating} and extra details {args}"
    return result


print(arbitrary_arguments("a", 3, "a", "r", "g", "s"))


def arbitrary_arguments_dic(prog_language, rating, **kwargs):
    """**kwarg return as dictionary"""
    kwargs["language"] = prog_language
    kwargs["star_rating"] = rating
    return kwargs


response = arbitrary_arguments_dic("python", 3, level="master", years_of_exp=5)
print(response)
