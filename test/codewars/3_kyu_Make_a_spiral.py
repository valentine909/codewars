"""
https://www.codewars.com/kata/make-a-spiral/train/python
"""


def is_out(position, size):
    return any(x > (size - 1) or x < 0 for x in position)


def is_one(position, matrix):
    return not is_out(position, len(matrix)) and matrix[position[0]][position[1]] == 1


def sum_coordinates(position, direction):
    return [sum(i) for i in zip(position, direction)]


def spiralize(size):
    matrix = [[0 for x in range(size)] for y in range(size)]
    directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]  # E, S, W, N
    cur_pos = [0, 0]
    while True:
        matrix[cur_pos[0]][cur_pos[1]] = 1
        try_pos = sum_coordinates(cur_pos, directions[0])  # Position which can be converted to "one"
        next_pos = sum_coordinates(try_pos, directions[0])  # Check if it is "one" already. Detect snake touch.
        if is_out(try_pos, size) or is_one(next_pos, matrix):
            directions.append(directions.pop(0))  # Change direction and return previous direction to pool
            try_pos = sum_coordinates(cur_pos, directions[0])
            next_pos = sum_coordinates(try_pos, directions[0])
            side_pos = sum_coordinates(try_pos, directions[1])  # When size is even and spiral is in the center.
                                                                # Detect side snake touch.
            if is_one(next_pos, matrix) or is_one(side_pos, matrix):
                break
        cur_pos = try_pos
    return matrix
