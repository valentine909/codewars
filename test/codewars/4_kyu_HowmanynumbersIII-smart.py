# abstraction used in this algorithm:
# |         |       |         |
# |         |       |         |
# |         |       |         |
# |         |  or   |        *|
# |         |       |      * *|
# |* * * * *|       |    * * *|
# |*_*_*_*_*|       |*_*_*_*_*|
# height of the box equals 9 (decimal base)
# width of the box equals length of the number
# sum of the digits is represented by the number of particles that fits the box
# should find all possible states when particle are evenly distributed or
# aligned to the right (border conditions)


def is_valid(sum_of_digits, number_length):
    # check if the input makes sense
    if sum_of_digits < number_length or sum_of_digits > number_length * 9:
        return False
    else:
        return True


def unique_list(sample_list):
    # produces list with unique values
    uni_list = []
    for item in sample_list:
        if item not in uni_list:
            uni_list.append(item)
    return uni_list


def find_states(sum_of_digits, number_length):
    set_of_states = set()
    first = 1
    for i in range(number_length):
        first += 10 ** (i + 1)
    set_of_states.add(first)
    print(first)
    temp = set()
    for i in range(sum_of_digits - number_length):
        for state in set_of_states:
            for j in range(number_length, 1, -1):
                if state % 10 ** j // 10 ** (j - 1) > state % 10 ** j:
                    temp.add()
            if state % 10 < 9:
                temp.add(state + 1)
        set_of_states = temp
        temp = set()
# def find_states(sum_of_digits, number_length):
#     list_of_states = [[1] * number_length]
#     temp = []
#     for i in range(sum_of_digits - number_length):
#         for state in list_of_states:
#             for j in range(number_length - 1):
#                 if state[j + 1] > state[j]:
#                     temp.append(state[:j] + [state[j]+1] + state[j+1:])
#             if state[-1] < 9:
#                 temp.append(state[:-1] + [state[-1] + 1])
#         list_of_states = unique_list(temp)
#         temp = []
#     return sorted(list_of_states)


def list_to_number(some_list):
    return int("".join(map(str, some_list)))


def find_all(sum_dig, digs):
    if not is_valid(sum_dig, digs):
        return []
    states = find_states(sum_dig, digs)
    if len(states) == 1:
        return [1, list_to_number(states[0]), list_to_number(states[0])]
    else:
        return [len(states), list_to_number(states[0]), list_to_number(states[-1])]



# print(find_all(10, 3))
# print(find_all(27, 3))
# print(find_all(60, 17))
find_states(10, 7)
