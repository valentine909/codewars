"""
https://www.codewars.com/kata/5426d7a2c2c7784365000783/python
"""


def balanced_parens(n: float, count=0) -> list:
    result = []
    if n == 0:
        return [""]
    elif 2 * n == count == 1:
        return [")"]
    elif 2 * n >= count > 0:
        result = ["(" + i for i in balanced_parens(n - 0.5, count=count + 1)] + \
                 [")" + i for i in balanced_parens(n - 0.5, count=count - 1)]
    elif 2 * n > count == 0:
        result = ["(" + i for i in balanced_parens(n - 0.5, count=count + 1)]
    return result
