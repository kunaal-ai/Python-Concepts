""" Example:
Input: "Python is my language"
Outout: "language my is Python"
"""

def reverse_string_words(user_string):
    """ return the string in reverse words order
    Args:
        user_String: (string)
    Return:
        return reveresed words
    """
    response = user_string.split(' ')[::-1]
    return " ".join(response)

print(reverse_string_words("Python is my language"))
