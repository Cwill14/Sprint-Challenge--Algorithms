'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
import re

# count = 0

def count_th(word):
# YOU CAN SOLVE THIS IN ONE LINE
    # return len(re.findall("th", word))  # <-------
# DON'T NEED RECURSION OR LOOPS, JUST USE REGEX ^^^
    # count = 0
    # count = 0
    # count = count
    # global count
    # if word has th
    # if word[0:2] == "th":
    # count += 1
        # print(f"count Before: {count}")
        # count += 1
        # print(f"count After: {count}")
    # word = [th:]
        # print(f"word Before: {word}")
        # word = word[2:]
        # print(f"word After: {word}")
        # return 1 + count_th(word)
        # return count
    # else:
        # return 0 
    #     count
        # return count
    # count_th(word)
    # count_th(word)
    # return 1 + count_th(word)
    # return count
    # print(f"word[0:1]: {word[0:2]}")
    # if 'th' not in word:
    #     return 0
    # else:
    #     word = word.replace('th',' ', 1)
    #     return 1 + count_th(word)
    if 'th' in word:
        word = word.replace('th', ' ', 1)
        return 1 + count_th(word)
    else:
        return 0



print(count_th("throw"))
print(count_th("thoth"))
print(count_th("Thanos"))
print(count_th("taught"))