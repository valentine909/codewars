"""
https://www.codewars.com/kata/strip-comments/train/python
"""


def solution(a, symbols):
    for i in symbols:
        while i in a:
            x, y = a.split(i, 1)
            if "\n" in y:
                a = x.strip(" ") + "\n" + y.split("\n", 1)[1]
            else:
                a = x.strip(" ")
    return a
