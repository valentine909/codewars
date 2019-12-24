"""
http://code.activestate.com/recipes/218332/
https://github.com/Orange9000/Codewars/blob/master/Solutions/beta/beta_how_many_numbers_iii.py
"""


def partitions(n):
    # base case of recursion: zero is the sum of the empty list
    if n == 0:
        yield []
        return

    # modify partitions of n-1 to form partitions of n
    for p in partitions(n - 1):
        yield [1] + p
        if p and (len(p) < 2 or p[1] > p[0]):
            yield [p[0] + 1] + p[1:]


def find_all(sum_dig: int, digs: int):
    if sum_dig < digs or sum_dig > digs * 9:
        return []
    data = [i for i in partitions(sum_dig) if len(i) == digs]
    data1 = sorted(["".join(map(str, a)) for a in data if len("".join(map(str, a))) == digs])
    # print(data1)
    return [len(data1), int(data1[0]), int(data1[-1])]


# print(find_all(35, 6))  # [123, 116999, 566666]
# print(find_all(10, 3))  # [8, 118, 334]
# print(find_all(16, 4))  # [27, 1159, 4444]
# print(find_all(25, 5))  # [73, 11599, 55555]
# print(find_all(11, 3))  # [10, 119, 344]
# print(find_all(11, 4))  # [11, 1118, 2333]
# print(find_all(15, 4))  # [23, 1149, 3444]
print(find_all(65, 17))  # [9049, 11111111111499999, 33333333444444444]
