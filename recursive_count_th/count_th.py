'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
import re

def count_th(word):
# YOU CAN SOLVE THIS IN ONE LINE
    return len(re.findall("th", word))  # <-------
# DON'T NEED RECURSION OR LOOPS, JUST USE REGEX ^^^
# why would you ever use recursion for something like this?
# seems like a lot of overcomplication
    # count = 0
    # ?
    


print(count_th("throw"))
print(count_th("thoth"))
print(count_th("Thanos"))
print(count_th("taught"))