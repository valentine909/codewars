"""
https://www.codewars.com/kata/5ff0fc329e7d0f0010004c03/train/python
"""


def count_diamonds(diamond_map, num_of_diamonds):
    parcels = []
    size = float('inf')
    for up in range(len(diamond_map)):
        inter_sum = [0] * len(diamond_map[0])
        for bottom in range(up, len(diamond_map)):
            inter_sum = [inter_sum[i] + diamond_map[bottom][i] for i in range(len(inter_sum))]
            for col1, col2 in _sliding_window_1d(inter_sum, num_of_diamonds):
                square_of_the_area = (bottom - up + 1) * (col2 - col1 + 1)
                if square_of_the_area < size:
                    size = square_of_the_area
                    parcels = [[(up, col1), (bottom, col2)]]
                elif square_of_the_area == size:
                    parcels.append([(up, col1), (bottom, col2)])
    return sorted(parcels)


def _sliding_window_1d(some_list: list, target_sum: int):
    current_sum = left = 0
    for right in range(len(some_list)):
        current_sum += some_list[right]
        while current_sum - some_list[left] >= target_sum:
            current_sum -= some_list[left]
            left += 1
        if current_sum == target_sum:
            yield left, right
