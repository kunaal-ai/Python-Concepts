"""pass
"""
def string_have_format(s):
    """Check for input if has asked all formats such as digit, lower etc
    and return T or False

    Args:
        s (str): user input
    """
    response = [False, False, False, False, False]

    for i in enumerate(s):
        if i[1].isalnum():
            response[0] = True
        if i[1].isalpha():
            response[1] = True
        if i[1].isdigit():
            response[2] = True
        if i[1].islower():
            response[3] = True
        if i[1].isupper():
            response[4] = True

    for i in response:
        print(i)


string_have_format('qA2')
