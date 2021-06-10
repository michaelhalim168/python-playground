'''
LONGEST WORD CHALLENGE DESCRIPTION:

In this challenge you need to find the longest word in a sentence. If the sentence has more than one word of the same length you should pick the first one.

INPUT SAMPLE:

Your program should accept as its first argument a path to a filename. Input example is the following

1 some line with text
2 another line

Each line has one or more words. Each word is separated by space char.

OUTPUT SAMPLE:
1 some
2 another

Print the longest word in the following way.
'''

def longest_word(str):
    return max(str.split(" "), key=len)

my_string = "some line with text"
print(longest_word(my_string))