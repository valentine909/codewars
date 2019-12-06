"""
https://www.codewars.com/kata/sum-of-intervals/train/python
"""
# Count of unique numbers in the intervals equals to
# length of overlapping intervals


def sum_of_intervals(list_of_tuples):
    set_of_numbers_in_interval = set()
    for tup in list_of_tuples:
        for number in range(tup[0], tup[1]):
            set_of_numbers_in_interval.add(number)
    return len(set_of_numbers_in_interval)


print(sum_of_intervals([(1, 4), (7, 10), (3, 5)]))
