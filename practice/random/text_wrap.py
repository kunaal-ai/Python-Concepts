""" Input:
ABCDEFGHIJKLIMNOQRSTUVWXYZ
4

Output:
ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ
"""

import textwrap

def text_wraping(string:str, max_width:int):
    """text wrap on user provided max_width

    Args:
        string (str): can be long string to wrap
        max_width (int): width to wrap the text

    Returns:
        list: return list with \n instead of blank space
    """
    res = textwrap.wrap(string, max_width)
    res = "\n".join(res)
    return res

print(text_wraping('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 4))
