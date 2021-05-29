"""
Create a function that determines whether or not it’s possible to split a pie fairly given these three parameters:
  - Total number of slices
  - Number of recipients
  - How many slices each person gets 

Form of the function:
    equal_slices(total_ slices, no_recipients, slices_each)

Examples:
    equal_slices(11, 5, 2) ➞ True
    5 people x 2 slices each = 10 slices < 11 slices 

    equal_slices(11, 5, 3) ➞ False
    5 people x 3 slices each = 15 slices > 11 slices


    equal_slices(8, 3, 2) ➞ True

    equal_slices(8, 3, 3) ➞ False

    equal_slices(24, 12, 2) ➞ True

Notes:
 - Return True if there are zero people.
 - It's fine not to use the entire pie.
 - All parameters are integers
"""


def equal_slices(total_slices, no_recipients, slices_each):
    if (no_recipients * slices_each) <= total_slices:
        return True
    else:
        return False


"""
Adjust the function 'equal_slices' from question_00 to return number of pieces left as well.

Examples:
    equal_slices(11, 5, 2) ➞ (True, 1)
    # 5 people x 2 slices each = 10 slices < 11 slices 

    equal_slices(11, 5, 3) ➞ (False,None)
    # 5 people x 3 slices each = 15 slices > 11 slicess

    equal_slices(8, 3, 2) ➞ (True, 2)

    equal_slices(8, 3, 3) ➞ (False, None)

    equal_slices(24, 12, 2) ➞ (True, 0)

Notes:
 - Return (True, total_slices) if there are zero people.
 - All parameters are integers.

"""
def equal_slices(total_slices, no_recipients, slices_each):
    if (no_recipients * slices_each) <= total_slices: 
        remaining = total_slices - (no_recipients * slices_each)
        return (True, remaining)
    else:
        return (False, None)

"""
Given two strings, create a function that returns the total number of unique characters from the combined string.

Examples:
    count_unique_chars("apple", "play") ➞ 5
    "appleplay" has 5 unique characters:  "a", "e", "l", "p", "y"

    count_unique_chars("sore", "zebra") ➞ 7

    count_unique_chars("a", "soup") ➞ 5

Notes:
 - Careful with empty strings
 - All characters will be lowercase.

"""
def count_unique_chars(string_1, string_2):
    return len(set((string_1 + string_2).strip()))

"""
Create a function that takes a string of lowercase characters and returns that string reversed and in upper case.

Examples:
    reverse_capitalize("abc") ➞ "CBA"

    reverse_capitalize("hellothere") ➞ "EREHTOLLEH"

    reverse_capitalize("input") ➞ "TUPNI"
"""

def reverse_capitalize(string):
    return string.upper()[::-1]

"""
Create a function that takes an integer and returns True if it's divisible by 100, otherwise return False.

Examples:
    divisible(1) ➞ False

    divisible(1000) ➞ True

    divisible(100) ➞ True

"""
def divisible(integer):
    return True if (integer % 100 == 0) else False