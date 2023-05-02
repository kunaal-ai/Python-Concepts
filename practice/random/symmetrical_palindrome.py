"""Given a string. the task is to check if the string is symmetrical and palindrome or not. 
A string is said to be symmetrical if both the halves of the string are the same and a string 
is said to be a palindrome string if one half of the string is the reverse of the other half or 
if a string appears same when read forward or backward.

Example: 

Input: khokho
Output: 
The entered string is symmetrical
The entered string is not palindrome

Input:amaama
Output:
The entered string is symmetrical
The entered string is palindrome
"""

def str_symmterical_palindrome(user_string):
    """ return if input string belongs to symmetrical,palindrome
    Args:
        user_string (string): user input
    Returns:
        print nature of string , either symmetrical,palindrome or both
    """
    center = len(user_string) // 2
    first_str = user_string[:center]
    second_str = user_string[center:]

    if first_str == second_str:
        print("Yes! The entered string is symmetrical")
    else:
        print("No! The entered string is NOT symmetrical")

    if first_str == second_str[::-1]:
        print("Yes! The entered string is palindrome")
    else:
        print("No! The entered string is NOT palindrome")


str_symmterical_palindrome("amaama")
