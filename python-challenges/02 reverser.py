'''
Challenge #2: Reverser Challenge
May 27, 2021

Given a standard input, writes each line reversed to standard output.
'''

import sys

n = sys.stdin.read()

def reverse(n):
    return n[::-1]

print(reverse(n))