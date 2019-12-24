"""
https://www.codewars.com/kata/strip-comments/train/python
"""


def solution(string, symbols):
    lst = string.split("\n")
    for symbol in symbols:
        for i in range(len(lst)):
            lst[i] = lst[i].split(symbol)[0].rstrip()
    return "\n".join(lst)
