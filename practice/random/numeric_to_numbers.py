""" Example:
convert "two one three" to 2 1 3 and return

"""

def numeric_to_numbers(user_string):
    """ Given a string S, containing numeric words, 
    the task is to convert 	the given string to the actual number.
    """
    dic = {
        "one": "1",
        "two": "2",
        "three": "3"
    }

    response_list = [ dic[i] for i in user_string.split(' ')  ]
    return " ".join(response_list)

print(numeric_to_numbers("two one three"))
