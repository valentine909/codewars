"""
https://www.codewars.com/kata/twice-linear/train/python
"""


def dbl_linear(n):
    u = {1}
    temp = set(u)
    count = 0
    while count < 4:
        for i in u:
            temp.add(2 * i + 1)
            temp.add(3 * i + 1)
        u = set(temp)
        if len(u) - 1 > n:
            count += 1
    u = sorted(u)
    return u[n]


print(dbl_linear(50))
