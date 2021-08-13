"""
https://www.codewars.com/kata/5aa859ad4a6b3408920002be/train/python
"""
from copy import deepcopy


def normalize(nested_list: list, growing_value: int = 0) -> list:
    dimension, size = _get_dimension_and_size(nested_list)
    my_list = deepcopy(nested_list)
    return _build_hypercubed_list(my_list, dimension, size, growing_value)


def _get_dimension_and_size(some_list: list, dimension: int = 0) -> tuple:
    sizes = [len(some_list)]
    dimensions = [dimension + 1]
    for element in some_list:
        if isinstance(element, list):
            dimension_tmp, size_tmp = _get_dimension_and_size(element, dimensions[0])
            dimensions.append(dimension_tmp)
            sizes.append(size_tmp)
    return max(dimensions), max(sizes)


def _build_hypercubed_list(some_list: list, dimension: int, size: int, filler: int) -> list:
    if dimension > 1:
        for i in range(size):
            try:
                if isinstance(some_list[i], list):
                    some_list[i].extend([filler] * (size - len(some_list[i])))
                else:
                    some_list[i] = [some_list[i]] * size
            except IndexError:
                some_list.append([filler] * size)
            some_list[i] = _build_hypercubed_list(some_list[i], dimension - 1, size, filler)
    return some_list
