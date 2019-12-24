"""
https://www.codewars.com/kata/snail/train/python
Straightforward solution.
"""


def snail(snail_map):
    directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]  # E, S, W, N
    path = []
    cur_pos = [0, 0]
    n = len(snail_map[0])  # Because of len([[]]) = 1
    while len(path) < n ** 2:
        path.append(cur_pos)
        try_pos = [sum(i) for i in zip(cur_pos, directions[0])]
        if any(x > (n - 1) or x < 0 for x in try_pos) or try_pos in path:  # If out of range or visited already
            directions.append(directions.pop(0))  # Change direction and return previous direction to pool
            try_pos = [sum(i) for i in zip(cur_pos, directions[0])]
        cur_pos = try_pos
    return [snail_map[i[0]][i[1]] for i in path] if path else []
