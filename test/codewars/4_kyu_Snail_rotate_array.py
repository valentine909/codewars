"""
https://www.codewars.com/kata/snail/train/python
"""


def snail(snail_map):
    result = []
    while snail_map:
        result += snail_map.pop(0)
        snail_map = [list(a) for a in zip(*[i[::-1] for i in snail_map])]  # Rotate array counter-clockwise
    return result
