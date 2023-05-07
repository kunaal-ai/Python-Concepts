"""print the number of times that the substring occurs in the given string. 
String traversal will take place from left to right, not from right to left. 
"""


def count_substring(string, sub_string):
    """ Find occurances of sub_string in given string
    Args:
        string: (string) - string value
        sub_string: (string) - that needs to be lookup in string 

    Return:
        int : find number of occurance of substring and return
    """
    count = 0
    for i in range(len(string)):
        if string[i:].startswith(sub_string):
            count += 1
    return count


print(count_substring('12jlka445kljakldfjlaksjdfdka3942', '3942'))
