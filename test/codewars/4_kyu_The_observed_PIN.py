"""
https://www.codewars.com/kata/the-observed-pin/train/python
"""
possible_keys_dict = {'1': ['1', '2', '4'],
                      '2': ['1', '2', '3', '5'],
                      '3': ['2', '3', '6'],
                      '4': ['1', '4', '5', '7'],
                      '5': ['2', '4', '5', '6', '8'],
                      '6': ['3', '5', '6', '9'],
                      '7': ['4', '7', '8'],
                      '8': ['0', '5', '7', '8', '9'],
                      '9': ['6', '8', '9'],
                      '0': ['8', '0']}


def calculate(observed):
    if len(observed) == 1:
        for i in possible_keys_dict[observed[0]]:
            yield i
    else:
        for i in possible_keys_dict[observed[0]]:
            for j in get_pins(observed[1:]):
                yield i + j


def get_pins(observed):
    return [i for i in calculate(str(observed))]


print(get_pins("369"))
