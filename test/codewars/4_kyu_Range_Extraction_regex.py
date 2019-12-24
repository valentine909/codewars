"""
https://www.codewars.com/kata/range-extraction/train/python

Algorithm is working but appears to be bulky. It utilizes the following steps:
1. Finding the differences between adjacent numbers.
2. Using Regex to find out two or more consequent 'ones' which means finding intervals.
3. Playing with sets to form a list (named 'full') of tuples (contain start-end
indexes) which is translated into final string.
Ex. of 'full': [(0, 0), (1, 5), (6, 8), (9, 13), (14, 14), (15, 15), (16, 19)]
(0,0) - index of standalone number
(1,5) - indexes of interval
"""


def find_differences(full_list):
    differences = ''
    for i in range(len(full_list) - 1):
        differences += str(full_list[i + 1] - full_list[i])
    return differences


def find_intervals(full_list):
    import re
    differences = find_differences(full_list)
    pattern = re.compile('[1]{2,}')  # Two or more 'ones' in differences means interval
    intervals = []
    for m in pattern.finditer(differences):
        intervals.append((m.start(), m.end()))
    return intervals


def find_full(full_list):
    intervals = find_intervals(full_list)
    full_set = {i for i in range(len(full_list))}
    intervals_set = set()
    for i in intervals:
        for j in range(i[0], i[1] + 1):
            intervals_set.add(j)
    standalone_set = full_set ^ intervals_set  # Indexes of numbers out of intervals
    standalone = []
    for i in standalone_set:
        standalone.append((i, i))
    full = sorted(intervals + standalone)  # Final list of tuples which is translated to string
    return full


def solution(full_list):
    full = find_full(full_list)
    result = ""
    for i in full:
        if i[0] == i[1]:
            result += str(full_list[i[0]]) + ','  # Standalone
        else:
            result += str(full_list[i[0]]) + '-' + str(full_list[i[1]]) + ','  # Intervals
    return result.rstrip(",")


a = [-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20]
print(solution(a))

