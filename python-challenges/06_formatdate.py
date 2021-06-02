'''
Create a function that converts a date formatted as MM/DD/YYYY to YYYYDDMM.
'''
def format_date(date):
    split_date = date.split('/')
    return split_date[2]+split_date[1]+split_date[0]

'''
Project Euler
'''

def prime_factor(num):
    factor = []
    i = 2
    while i <= num:
        if n%i==0:
            